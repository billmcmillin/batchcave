from django.db import models
from django.core.files import File
from django.core.files.storage import FileSystemStorage
import datetime
from converter.modelsdir import batchEdits
import inspect
from django.conf import settings

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
    upload_storage = FileSystemStorage(location=settings.MEDIA_ROOT, base_url='/data')
    Upload = models.FileField(upload_to='infiles/', storage=upload_storage, default=None)
    Output = models.FileField(upload_to='outfiles/', storage=upload_storage, default='outfiles/TEST.mrc')

    def clean(self):
        if self.Upload is None:
            raise ValidationError(_('Each conversion must have a file uploaded.'))

    def check_file(self):
        pass
