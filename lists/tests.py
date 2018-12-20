from django.test import TestCase
from django.urls import resolve
from lists.views import landing_page

class LandingPageTest(TestCase):

    def test_root_url_resolves_to_landing_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, landing_page)
