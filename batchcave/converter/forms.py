from django import forms
from converter.models import Conversion

class ConversionForm(forms.ModelForm):
    class Meta:
        model = Conversion
        fields = ('Name', 'Type', 'Upload',)
