from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse, resolve
# from .forms import CustomUserCreationForm
# from .views import SignupPageView


class CustomUserTests(TestCase):

    # testing for creating a new user
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

    # testing for creating a new super user
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


# class SignupPageTests(TestCase):
#
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)
#
#     # testing if the signup is using the signup.html and it contains the content Sign Up and does not contains the content yemi
#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'signup.html')
#         self.assertContains(self.response, 'Sign Up')
#         self.assertNotContains(self.response, 'yemi')
#
#     # testing if the sign up form uses the CustomUserCreationForm form and it contains the csrfmiddlewaretoken
#     def test_signup_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')
#
#     # testing if the accounts/signup rout uses the SignupPageView view in views.py
#     def test_signup_view(self): # new
#         view = resolve('/accounts/signup/')
#         self.assertEqual(
#         view.func.__name__,
#         SignupPageView.as_view().__name__
#         )


# the updated test after using django allauth for signup
class SignupTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)
