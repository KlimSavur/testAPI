from tastypie.resources import ModelResource
from api.models import Task

class TaskResource(ModelResources):
    class Meta:
        queryset = Task.objects.all()
        resource_name = "task"
