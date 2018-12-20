from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import landing_page

class LandingPageTest(TestCase):

    def test_root_url_resolves_to_landing_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, landing_page)

    def test_landing_page_returns_correct_html(self):
        request = HttpRequest()
        response = landing_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
