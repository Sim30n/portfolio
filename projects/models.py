from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    code = models.URLField(blank=True)
    date = models.CharField(max_length=50)
    ## Points to a Cloudinary image
    image = CloudinaryField('image')
