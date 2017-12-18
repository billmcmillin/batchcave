from django.test import TestCase
from converter.models import Conversion
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from pymarc import MARCReader
import pymarc
from django.utils.html import escape

class HomePageTest(TestCase):

    def get_test_file(self):
        with open('/code/batchcave/converter/infiles/TEST.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('testing_upload.txt', testMarc.read())
        return test_file

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>BatchCave</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'converter/home.html')

    def test_validation_errors_are_sent_to_base_template(self):
        test_file = self.get_test_file()
        response = self.client.post('/conversions/create/', data={'Name':'','Type': 1, 'Upload': test_file})
        expected_error = escape("The Conversion could not be created because the data didn't validate.")
        self.assertContains(response, expected_error)
