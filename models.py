from django.db import models

# Create your models here.
class job(models.Model):
    gender=(('male','male'),('female','female'))
    name=models.CharField(max_length=30)
    Education_Qualification=models.CharField(max_length=30)
    Experience=models.CharField(max_length=30)
    age=models.IntegerField()
    skills=models.CharField(max_length=100,default='')
    gender=models.CharField(max_length=30,choices=gender)
    About=models.CharField(max_length=500)
    image = models.ImageField(upload_to='job_t_u/images/')

class profile(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    headline=models.CharField(max_length=100)
    current_postion=models.CharField(max_length=100)
    education=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)