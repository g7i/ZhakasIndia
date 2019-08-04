from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
   
    def __str__(self):
        return self.name

class Community(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Communities'

    def __str__(self):
        return self.name