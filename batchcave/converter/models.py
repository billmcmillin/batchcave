from django.db import models
from django.core.files import File
from django.core.files.storage import FileSystemStorage
import datetime
from django.conf import settings

class Conversion(models.Model):
    Name = models.TextField(default='')
    Type = models.TextField(default='')
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
