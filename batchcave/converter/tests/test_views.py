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

