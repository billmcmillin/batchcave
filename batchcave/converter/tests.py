from django.test import TestCase
from converter.models import Conversion
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>BatchCave</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'converter/home.html')

class ConversionModelTest(TestCase):

    def test_get_error_from_invalid_input(self):
        response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': None})
        self.assertEqual(Conversion.objects.count(), 0)

    def test_get_error_from_invalid_model(self):
        with self.assertRaises(ValidationError):
            Conversion(Name='Test1', Type=0, Upload=None).save()

    def test_saving_and_retrieving_job(self):
        pass

class NewConversionTest(TestCase):
    def test_only_saves_when_necessary(self):
        self.client.get('/conversions/create')
        self.assertEqual(Conversion.objects.count(), 0)

    #NOTE: this will only work from inside the container
    def test_can_save_new_conversion(self):
        with open('batchcave/converter/infiles/TEST.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('testing_upload.txt', testMarc.read())
        response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': test_file})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Conversion.objects.count(), 1)
        new_item = Conversion.objects.first()
        self.assertEqual(new_item.Type, 1)

        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], 'conversions')

