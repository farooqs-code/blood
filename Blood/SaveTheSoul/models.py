from django.db import models

# Create your models here.

class DonorInfo(models.Model):
    donor_name = models.CharField(max_length=30)
    password = models.TextField(max_length=14)
    age = models.IntegerField()
    contact = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(max_length=300)
    blood_group = models.TextField()
    address = models.TextField()
    Last_donoted_date = models.DateField()


