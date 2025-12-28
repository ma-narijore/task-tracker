from django.urls import path

from .views import (
    index,
    TasksView,
    TasksDetailView,
    TasksCreateView,
    TasksUpdateView,
    TasksDeleteView,
    WorkersView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TasksView.as_view(), name="tasks"),
    path("tasks/<int:pk>/", TasksDetailView.as_view(), name="tasks-detail"),
    path("tasks/create/", TasksCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/update/", TasksUpdateView.as_view(),
         name="tasks-update"),
    path("tasks/<int:pk>/delete/", TasksDeleteView.as_view(),
         name="tasks-delete"),
    path("workers/", WorkersView.as_view(), name="workers"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(),
         name="workers-detail"),
    path("workers/create/", WorkerCreateView.as_view(),
         name="workers-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(),
         name="workers-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(),
         name="workers-delete"),

]

app_name = "app"
