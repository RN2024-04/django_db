from django.db import models

# Create your models here.
class Buyer(models.Model):
    name=models.CharField(max_length=100)
    balance=models.DecimalField(decimal_places=100,max_digits=100)
    age=models.IntegerField()



class Game(models.Model):
    title=models.CharField(max_length=100)
    cost=models.DecimalField(decimal_places=100,max_digits=100)
    description=models.TextField()
    age_limited=models.BooleanField(False)
    buyer=models.ManyToManyField(Buyer,related_name="games")



 # python manage.py makemigrations
 # python manage.py migrate