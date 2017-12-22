from django.test import TestCase
from converter.models import Conversion
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from pymarc import MARCReader
import pymarc
import time

class ConversionModelTest(TestCase):

    def get_bad_file(self):
        with open('/code/batchcave/converter/infiles/BADTEST.mrc', 'rb') as testMarc:
        #with open('/code/batchcave/converter/infiles/shell.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('testing_bad_upload.mrc', testMarc.read())
        return test_file

    def get_corrupt_file(self):
        with open('/code/batchcave/converter/infiles/CORRUPTTEST.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('testing_bad_upload.mrc', testMarc.read())
        return test_file

    def test_get_error_from_incomplete_input(self):
        with self.assertRaises(ValueError):
            response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': None})
        self.assertEqual(Conversion.objects.count(), 0)

    def test_get_error_from_invalid_model(self):
        with self.assertRaises(ValueError):
            Conversion(Name='Test1', Type=0, Upload=None).save()

    def test_cannot_save_incomplete_conversion(self):
        conv = Conversion.objects.create()
        with self.assertRaises(ValueError):
            conv.save()

    def test_only_marc_file_can_be_uploaded(self):
        bad_file = self.get_bad_file()
        with self.assertRaises(ValidationError):
            conv = Conversion.objects.create()
            conv.Name = "Bad Conversion"
            conv.Type = 1
            conv.Upload = bad_file
            conv.save()

    #marc file with data missing in teh middle cannot be uploaded
    def test_only_complete_marc_file_can_be_uplaoded(self):
        corrupt_file = self.get_corrupt_file()
        with self.assertRaises(ValidationError):
            conv = Conversion.objects.create()
            conv.Name = "Corrupt Conversion"
            conv.Type = 1
            conv.Upload = corrupt_file
            conv.save()

class NewConversionTest(TestCase):
    def get_test_file(self):
        with open('/code/batchcave/converter/infiles/TEST.mrc', 'rb') as testMarc:
            test_file = SimpleUploadedFile('TEST.mrc', testMarc.read())
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
        response = self.client.post('/conversions/create/', data={'Name':'Redirect?','Type': 1, 'Upload': test_file})
        print(response)
        self.assertEqual(response['location'], '/conversions/')

    def test_displays_all_conversions(self):
        test_file = self.get_test_file()
        self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': test_file})
        response1 = self.client.get('/conversions/')
        self.assertIn('First one', response1.content.decode())


    def test_conversion_outfile_is_saved(self):
        good_file = self.get_test_file()
        response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': good_file})
        first_one = Conversion.objects.first()
        inreader = MARCReader(first_one.Upload)
        outreader = MARCReader(first_one.Output)
        in_titles = []
        out_titles = []
        for record in inreader:
            in_titles.append(str(record['245']))
        for record in outreader:
            out_titles.append(str(record['245']))
        self.assertEqual(in_titles[0], out_titles[0])

    def test_conversion_outfile_is_visible(self):
        good_file = self.get_test_file()
        response = self.client.post('/conversions/create/', data={'Name':'First one','Type': 1, 'Upload': good_file})
        response1 = self.client.get('/conversions/')
        print(response1)
        self.assertIn('Download Result', response1.content.decode())




