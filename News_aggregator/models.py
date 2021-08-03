from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=400)
    img=models.URLField(max_length=500)
    link=models.URLField(max_length=600)
    def __str__(self):
        return self.title