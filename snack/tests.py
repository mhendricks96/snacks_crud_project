from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack
# Create your tests here.


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="pickle", description="description test", purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "pickle")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "description test")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, f"Purchaser: {self.snack.purchaser}")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("create_snack"),
            {
                "title": "Raker",
                "description": "test",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_list"))
        self.assertContains(response, "Raker")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update_snack", args="1"),
            {"title": "Updated name","description":"new description","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_list"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("delete_snack", args="1"))
        self.assertEqual(response.status_code, 200)

