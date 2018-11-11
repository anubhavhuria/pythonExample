from django.db import models

class Pet(models.Model):
    SEX_CHOICES=[('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    spieces = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    age = models.IntegerField(null=True)
    submission_date = models.DateTimeField()
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)