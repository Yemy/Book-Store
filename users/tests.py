from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username='yemi',
        email='yemy@gmail.com',
        password='2992test'
        )
        self.assertEqual(user.username, 'yemi')
        self.assertEqual(user.email, 'yemy@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@gmail.com',
        password='2992admin'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
