from django.db import models

# Create your models here.

class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    cpopulation=models.IntegerField()
    
class Capital(models.Model):
    cname=models.ForeignKey(Country,on_delete=models.CASCADE)
    capitalname=models.CharField(max_length=100,primary_key=True)
    capitalpopulation=models.IntegerField()
    
class State(models.Model):
    capitalname=models.ForeignKey(Capital,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100,primary_key=True)
    spopulation=models.IntegerField()
    
class District(models.Model):
    sname=models.ForeignKey(State,on_delete=models.CASCADE)
    dname=models.CharField(max_length=100)
    dpopulation=models.IntegerField()