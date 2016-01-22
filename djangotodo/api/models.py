import logging

class ToDo(object):
    def __init__(self, *args, **kw):
        self.id = 0
        self.updated_by = ''
        self.updated_at = None
        self.text = ''


class ToDoList(object):
    """
    Used to add a root element to a returned array (to mitigate JSON Hijacking)
    """
    def __init__(self):
        self.items = []


class InMemoryStore(object):
    __list = []
    __counter = 0

    @staticmethod
    def list():
        return list(InMemoryStore.__list)

    @staticmethod
    def add(obj):
        InMemoryStore.__counter += 1
        obj.id = InMemoryStore.__counter
        InMemoryStore.__log('Adding object with id: %d' % obj.id)
        InMemoryStore.__list.append(obj)

    @staticmethod
    def get(id):
        InMemoryStore.__log('Getting object with id: %d' % id)

        for obj in InMemoryStore.__list:
            if obj.id == id:
                return obj

        InMemoryStore.__log('Object with id: %d not found!' % id)
        raise IndexError

    @staticmethod
    def delete(id):
        obj = InMemoryStore.get(id)
        InMemoryStore.__log('Deleting object with id: %d' % id)
        InMemoryStore.__list.remove(obj)

    @staticmethod
    def __log(message):
        logger = logging.getLogger(__name__)
        logger.debug(message)