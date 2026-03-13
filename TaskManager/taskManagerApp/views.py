from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by("-created_date")
    serializer_class = TaskSerializer

    def get_queryset(self):

        queryset = Task.objects.all()

        priority = self.request.query_params.get("priority")

        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset