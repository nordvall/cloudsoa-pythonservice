import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import ToDoSerializer, ToDoListSerializer
from models import ToDoList, InMemoryStore


class ToDoList(APIView):
    def get(self, request, format=None):
        self.log(request)
        todos = ToDoList()
        todos.items = InMemoryStore.list()
        serializer = ToDoListSerializer(todos)

        return Response(serializer.data)

    def post(self, request, format=None):
        self.log(request)
        serializer = ToDoSerializer(data=request.data)

        if serializer.is_valid():
            todo = serializer.save(updated_by=request.user.pk)
            InMemoryStore.add(todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def log(self, request):
        logger = logging.getLogger(__name__)
        logger.debug("Request by: " + str(request.user.pk))
        logger.debug("Payload: " + str(request.body))


class ToDoDetail(APIView):
    def get(self, request, pk, format=None):
        self.log(request)
        try:
            todo = InMemoryStore.get(int(pk))
            serializer = ToDoSerializer(todo)
            return Response(serializer.data)
        except IndexError:
            return Http404()

    def put(self, request, pk, format=None):
        self.log(request)
        todo = InMemoryStore.get(int(pk))
        serializer = ToDoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save(updated_by=request.user.pk)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.log(request)
        InMemoryStore.delete(int(pk))
        return Response(status=status.HTTP_204_NO_CONTENT)

    def log(self, request):
        logger = logging.getLogger(__name__)
        logger.debug("Request by: " + request.user.pk)
        logger.debug("Payload: " + request.body)