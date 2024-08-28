from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(title='First post')

    def test_model_content(self):
        self.assertEqual(self.post.title,'First post')

    def test_url_correct_locations_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage(self):  # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "Message Board Homepage")

    
