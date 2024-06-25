from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    des = models.TextField()

    def __str__(self):
        return self.name
