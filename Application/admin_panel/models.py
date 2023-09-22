from django.db import models

# Create your models here.
class AndroidApp(models.Model):
    
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=100)

    def __str__(self):
        return self.name
