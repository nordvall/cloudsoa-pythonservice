from datetime import datetime

class ToDo(object):
    def __init__(self, *args, **kw):
        self.id = 0
        self.updated_by = ''
        self.updated_at = None
        self.text = ''


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
        InMemoryStore.__list.append(obj)

    @staticmethod
    def get(id):
        for obj in InMemoryStore.__list:
            if obj.id == id:
                return obj

        raise IndexError

    @staticmethod
    def delete(id):
        obj = InMemoryStore.get(id)
        InMemoryStore.__list.remove(obj)