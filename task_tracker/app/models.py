from django.contrib.auth.models import AbstractUser
from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("HIGH", "High"),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=15,
        choices=PRIORITY_CHOICES,
        default="MEDIUM",
    )
    task_type = models.ForeignKey(
        "TaskType",
        on_delete=models.SET_NULL,
        null=True,
    )
    assignees = models.ManyToManyField(
        "Worker",
        related_name="assigned_tasks"
    )


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        "Position",
        on_delete=models.SET_NULL,
        null=True,
    )


class Position(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
