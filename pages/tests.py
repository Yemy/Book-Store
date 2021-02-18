from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


# class HomepageTests(SimpleTestCase):
#
#     # testing if the URL at / is OK
#     def test_homepage_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#         # testing if the name home for the homepage rout is correct
#     def test_homepage_url_name(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#
#         # testing if the HomePage is using the home.html template
#     def test_homepage_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'home.html')
#
#         # testing if the html page contains the content HomePage
#     def test_homepage_contains_correct_html(self):
#         response = self.client.get('/')
#         self.assertContains(response, 'Homepage')
#
#         # testing that the html page does not contain the content yemi
#     def test_homepage_does_not_contain_incorrect_html(self):
#         response = self.client.get('/')
#         self.assertNotContains(
#         response, 'yemi')

# a test using setup method for decreasing the prone to errors as we are repeating the response variable
class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'yemi')

        # testing if the / url path is using the function HomePageView in views.py
    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        self.assertEqual(
        view.func.__name__,
        HomePageView.as_view().__name__
        )
