from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_for_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')
