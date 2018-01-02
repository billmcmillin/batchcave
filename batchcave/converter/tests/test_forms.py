from django.test import TestCase
from converter.forms import ConversionForm, EMPTY_ITEM_ERROR

class ConversionFormTest(TestCase):

    def test_form_name_input_has_placeholder_and_css(self):
        form = ConversionForm()
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        with self.assertRaises(Exception) as e:
            form = ConversionForm(data={'Name': '','Type': '', 'Upload': ''})
            form.save()
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['Name'],
            [EMPTY_ITEM_ERROR]
        )
