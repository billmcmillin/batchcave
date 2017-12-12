from django.test import TestCase
from converter.models import Conversion
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from pymarc import MARCReader
import pymarc
import time

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
    def get_test_file(self):
        with open('/code/batchcave/converter/infiles/TEST.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('testing_upload.txt', testMarc.read())
        return test_file

    def get_bad_file(self):
        with open('/code/batchcave/converter/infiles/BADTEST.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('testing_bad_upload.mrc', testMarc.read())
        return test_file

    def test_only_saves_when_necessary(self):
        self.client.get('/conversions/create')
        self.assertEqual(Conversion.objects.count(), 0)

    #NOTE: this will only work from inside the container
    def test_can_save_new_conversion(self):
        test_file = self.get_test_file()
        response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': test_file})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Conversion.objects.count(), 1)
        new_item = Conversion.objects.first()
        self.assertEqual(new_item.Type, 1)

    def test_redirects_after_post(self):
        test_file = self.get_test_file()
        response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': test_file})
        self.assertEqual(response['location'], '/conversions/')

    def test_displays_all_conversions(self):
        test_file = self.get_test_file()
        self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': test_file})
        response1 = self.client.get('/conversions/')
        self.assertIn('First one', response1.content.decode())

    def test_only_marc_file_can_be_uploaded(self):
        good_file = self.get_test_file()
        bad_file = self.get_bad_file()
        bad_reader = MARCReader(bad_file)
        res = next(bad_reader)
        self.assertIn('Valu1e', res)
