from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class EmbarqueViewsUnitTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser(
            username="paanc",
            password="testing321",
        )
        self.credentials={"username":"admin","password":"testing321"}

    def test_home_link(self):
        url = reverse("embarques-home")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


