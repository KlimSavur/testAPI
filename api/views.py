from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.settings import api_settings
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializer import TaskSerializer, TokenSerializer
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class api_view(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,  request):
        Tasks = Task.objects.all()
        serializer = TaskSerializer(Tasks, many = True)
        return Response(serializer.data)
    def post(self, request):
        Task_data = request.data
        serializer = TaskSerializer(data=Task_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class api_detail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        task_data = request.data
        serializer = TaskSerializer(task, data=task_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class login_view(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data = { "token" : jwt_encode_handler(jwt_payload_handler(user))})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
class register_view(CreateAPIView):
     permission_classes = (AllowAny,)

     def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)
