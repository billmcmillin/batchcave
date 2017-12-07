from django.db import models
from django.core.files import File
from django.core.files.storage import FileSystemStorage
import datetime
from converter.modelsdir import batchEdits
import inspect
from django.conf import settings

class Conversion(models.Model):
    Name = models.TextField(default='')
    TYPE_CHOICES = [
            (0, 'None'),
    ]
    functions = inspect.getmembers(batchEdits.batchEdits, inspect.isfunction)
    for idx, item in enumerate(functions):
        TYPE_CHOICES.append((idx, item[0]))
    Type = models.IntegerField(choices=TYPE_CHOICES,default=0)
    TimeExecuted = models.DateTimeField(null=True)
    #NOTE - ensure this is outside the server doc root
    upload_storage = FileSystemStorage(location=settings.MEDIA_ROOT, base_url='/data')
    Upload = models.FileField(upload_to='infiles/', storage=upload_storage, default='infiles/TEST.mrc')
    Output = models.FileField(upload_to='outfiles/', storage=upload_storage,
default='outfiles/TEST.mrc')

    #construct with Conversion(Name=x, Type=y, Upload=z)

    def execute(self):
        try:
            self.TimeExecuted = datetime.datetime.now()
        except:
            result = 'Error'
        return result

    def check_file(self):
        pass
