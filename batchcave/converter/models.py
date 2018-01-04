from django.db import models
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import datetime
from converter.modelsdir import batchEdits
import inspect
from django.conf import settings
import pymarc
from pymarc import MARCReader

class ValidateOnSaveMixin(object):
#from https://www.xormedia.com/django-model-validation-on-save/
    def save(self, force_insert=False, force_update=False, **kwargs):
        if not (force_insert or force_update):
            self.TimeExecuted = datetime.datetime.now(datetime.timezone.utc)
            self.full_clean()
        super(ValidateOnSaveMixin, self).save(force_insert, force_update,
**kwargs)

class Conversion(ValidateOnSaveMixin, models.Model):
    Name = models.TextField(default='')
    TYPE_CHOICES = [
            (0, 'None'),
    ]
    functions = inspect.getmembers(batchEdits.batchEdits, inspect.isfunction)
    for idx, item in enumerate(functions):
        TYPE_CHOICES.append((idx+1, item[0]))
    Type = models.IntegerField(choices=TYPE_CHOICES,default=0)
    TimeExecuted = models.DateTimeField(null=True)
    #NOTE - ensure this is outside the server doc root
    upload_storage = FileSystemStorage(location=settings.MEDIA_ROOT,
base_url='/data')
    download_storage = FileSystemStorage(location="/code/batchcave/converter/",
base_url='')
    Upload = models.FileField(upload_to='infiles/', storage=upload_storage,
default=None)
    Output = models.FileField(upload_to='outfiles/', storage=download_storage,
default=None)
    RecordsIn = models.PositiveIntegerField(default=0)
    RecordsOut = models.PositiveIntegerField(default=0)

    def check_file(self):
        check_reader = MARCReader(self.Upload)
        try:
            for record in check_reader:
                self.RecordsIn += 1
        except:
            return 1
        self.make_conversion()
        return 0

    def clean(self):
        if self.Name is None:
            raise ValidationError('Each conversion must have a name.')
        if self.Upload is None:
            raise ValidationError('Each conversion must have a file uploaded.')
        if self.check_file() != 0:
            raise ValidationError('MARC file does not validate')
        if self.Type == 0:
            raise ValidationError('Type must not be none.')

    def make_conversion(self):
        conv_file = self.Upload
        django_file = File(conv_file)
        self.Output.save("Conversion_Results.mrc", django_file, save=False)
