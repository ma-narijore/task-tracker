from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import Task, TaskType, Position


class ModelStrTests(TestCase):

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="Bug")
        self.assertEqual(str(task_type), "Bug")

    def test_position_str(self):
        position = Position.objects.create(name="Developer")
        self.assertEqual(str(position), "Developer")


class TaskModelTests(TestCase):

    def test_task_assignees(self):
        user = get_user_model().objects.create_user(
            username="john",
            password="pass"
        )

        task_type = TaskType.objects.create(name="Feature")

        task = Task.objects.create(
            name="Implement login",
            deadline=timezone.now(),
            task_type=task_type
        )

        task.assignees.add(user)

        self.assertIn(user, task.assignees.all())
        self.assertIn(task, user.assigned_tasks.all())


class BaseViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            password="password"
        )

    def setUp(self):
        self.client.login(username="testuser", password="password")


class IndexViewTests(BaseViewTest):

    def test_index_context(self):
        response = self.client.get(reverse("app:index"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("num_tasks", response.context)
        self.assertIn("num_workers", response.context)


class TaskListViewTests(BaseViewTest):

    def test_task_list_view(self):
        response = self.client.get(reverse("app:tasks"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object_list"].count(), 0)


class TaskDetailViewTests(BaseViewTest):

    def test_task_detail_view(self):
        task_type = TaskType.objects.create(name="Bug")

        task = Task.objects.create(
            name="Fix bug",
            deadline=timezone.now(),
            task_type=task_type
        )

        response = self.client.get(
            reverse("app:tasks-detail", kwargs={"pk": task.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], task)


class TaskCreateViewTests(BaseViewTest):

    def test_task_create(self):
        task_type = TaskType.objects.create(name="Feature")

        worker = get_user_model().objects.create_user(
            username="worker",
            password="pass"
        )

        response = self.client.post(
            reverse("app:tasks-create"),
            {
                "name": "New task",
                "description": "Test description",
                "deadline": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                "priority": "HIGH",
                "task_type": task_type.id,
                "assignees": [worker.id],
                "is_complete": False,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="New task").exists())


class WorkerListViewTests(BaseViewTest):

    def test_worker_list_view(self):
        response = self.client.get(reverse("app:workers"))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, response.context["object_list"])


class WorkerDetailViewTests(BaseViewTest):

    def test_worker_detail_view(self):
        response = self.client.get(
            reverse("app:workers-detail", kwargs={"pk": self.user.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.user)


class LoginRequiredTests(TestCase):

    def test_tasks_requires_login(self):
        response = self.client.get(reverse("app:tasks"))
        self.assertEqual(response.status_code, 302)
