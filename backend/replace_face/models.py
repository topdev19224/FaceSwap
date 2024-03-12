from django.db import models

# Create your models here.
class FaceReplace(models.Model):
    image = models.ImageField(upload_to='upload/images/')
    video = models.FileField(upload_to='upload/videos/')
