from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Task, Worker
from .forms import WorkerCreationForm, WorkerUpdateForm


# Create your views here.
@login_required
def index(request):
    """View function for the home page of the site."""
    num_tasks = Task.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
    }
    return render(request, "app/index.html", context=context)


class TasksView(LoginRequiredMixin, ListView):
    """View function for the list of all tasks."""
    model = Task


class TasksDetailView(LoginRequiredMixin, DetailView):
    """View function for the detail view of a task."""
    model = Task


class TasksCreateView(LoginRequiredMixin, CreateView):
    """View function for the create view of a task."""
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:tasks")


class TasksUpdateView(LoginRequiredMixin, UpdateView):
    """View function for the create view of a task."""
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:tasks")


class TasksDeleteView(LoginRequiredMixin, DeleteView):
    """View function for the delete view of a task."""
    model = Task
    success_url = reverse_lazy("app:tasks")


class WorkersView(LoginRequiredMixin, ListView):
    """View function for the list of all workers."""
    model = Worker


class WorkerDetailView(LoginRequiredMixin, DetailView):
    """View function for the detail view of a worker."""
    model = Worker


class WorkerCreateView(LoginRequiredMixin, CreateView):
    """View function for the create view of a worker."""
    model = get_user_model()
    form_class = WorkerCreationForm
    success_url = reverse_lazy("app:workers")


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    """View function for the update view of a worker."""
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("app:workers")


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    """View function for the delete view of a worker."""
    model = Worker
    success_url = reverse_lazy("app:workers")
