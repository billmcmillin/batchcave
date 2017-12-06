from django.test import TestCase
from converter.models import Conversion


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>BatchCave</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'converter/home.html')

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

class NewConversionTest(TestCase):

    def test_can_save_new_conversion(self):
        response = self.client.post('/conversions/create/', data={'Name': 'First one','Type': 'ER_EAI_2nd'})
        self.assertEqual(Conversion.objects.count(), 1)
        new_item = Conversion.objects.first()
        self.assertEqual(new_item.Type, 'ER_EAI_2nd')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], 'conversions')

    def test_only_saves_when_necessary(self):
        self.client.get('/conversions/create')
        self.assertEqual(Conversion.objects.count(), 0)
