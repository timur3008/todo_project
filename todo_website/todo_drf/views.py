from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.models import User

from drf_yasg.utils import swagger_auto_schema

from todo_app.models import Todo
from todo_drf.serializers import TodoSerializer


# class TodoViewSet(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Todo.objects.filter(author=self.request.user)
    
#     def perform_create(self, serializer):
#         return serializer.save(author=self.request.user)
    

# class TodoListCreateView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request: HttpRequest):
#         todos = Todo.objects.filter(author=request.user)
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request: HttpRequest):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class TodoDetailView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_object(self, pk: int, user: User):
#         return get_object_or_404(Todo, pk=pk, author=user)
    
#     def get(self, request: HttpRequest,pk: int):
#         todo = self.get_object(pk=pk, user=request.user)
#         serializer = TodoSerializer(todo) # Сериализуй (преобразуй) этот объект(todo) в JSON
#         return Response(serializer.data, status=status.HTTP_200_OK)
#         # serializer.data - Преобразует объект Python → словарь
#         # Response(...) - Возвращает JSON-ответ пользователю API
    
#     def put(self, request: HttpRequest, pk: int):
#         todo = self.get_object(pk=pk, user=request.user)
#         serializer = TodoSerializer(todo, data=request.data) # обновление
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request: HttpRequest, pk: int):
#         todo = self.get_object(pk=pk, user=request.user)
#         serializer = TodoSerializer(todo, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request: HttpRequest, pk: int):
#         todo = self.get_object(pk=pk, user=request.user)
#         todo.delete()
#         return Response({'detail': 'Успешно удалено'}, status=status.HTTP_204_NO_CONTENT)


class TodoListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest):
        todos = Todo.objects.filter(author=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TodoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest, pk: int):
        todo = get_object_or_404(Todo, pk=pk, author=request.user)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=TodoSerializer)
    def post(self, request: HttpRequest):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=TodoSerializer)
    def put(self, request: HttpRequest, pk: int):
        todo = get_object_or_404(Todo, pk=pk, author=request.user)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoPatchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=TodoSerializer)
    def put(self, request: HttpRequest, pk: int):
        todo = get_object_or_404(Todo, pk=pk, author=request.user)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TodoDeleteView(APIView):
    permisson_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={200: 'Успешно удалено'})
    def delete(self, request: HttpRequest, pk: int):
        todo = get_object_or_404(Todo, pk=pk, author=request.user)
        todo.delete()
        return Response({'detail': 'Успешно удалено'}, status=status.HTTP_204_NO_CONTENT)