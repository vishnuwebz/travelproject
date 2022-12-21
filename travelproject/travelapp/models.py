from django.db import models

# Create your models here.
class Languages(models.Model):
    lname= models.CharField(max_length=250)
    limg= models.ImageField(upload_to='language_pics')
    ldesc= models.TextField()

    def __str__(self):
        return self.lname

class Programmers(models.Model):
    pname= models.CharField(max_length=250)
    pimg= models.ImageField(upload_to='programmers_pics')
    pdesc= models.TextField()

    def __str__(self):
        return self.pname