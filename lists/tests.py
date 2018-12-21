from django.test import TestCase

class LandingPageTest(TestCase):

    def test_uses_landing_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'landing.html')
