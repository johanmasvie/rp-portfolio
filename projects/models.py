from django.db import models

class Project(models.Model):
    title           = models.CharField(max_length=200)
    description     = models.TextField()
    technology      = models.CharField(max_length=20)
    image           = models.ImageField(upload_to="upload/", blank=True)