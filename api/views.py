from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializer import TaskSerializer
from .models import Task
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

