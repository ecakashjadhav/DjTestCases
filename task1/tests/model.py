from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User

class TestAppModel(TestCase):
    def test_model_str(self):
        title = Post.objects.create(title="django testing")
        content = Post.objects.create(content="this is some content")
        self.assertEqual(str(title), "django testing")

    def test_post_like_user(self):
        testuser = User.objects.create_user(username="testuser",password="12345")
        testuser2 = User.objects.create_user(username="testuser2",password="12345")
        title = Post.objects.create(title="django",content="this is some content")
        title.likes.set([testuser.pk,testuser2.pk])
        self.assertEqual(title.likes.count(), 2)