from django.test import TestCase
from converter.models import Conversion


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>BatchCave</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

class ConversionModelTest(TestCase):

    def test_saving_and_retrieving_job(self):
        first_item = Conversion()
        first_item.Name = 'First process run'
        first_item.save()

        second_item = Conversion()
        second_item.Name = 'Second process run'
        second_item.save()

        saved_items = Conversion.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.Name, 'First process run')
        self.assertEqual(second_saved_item.Name, 'Second process run')
