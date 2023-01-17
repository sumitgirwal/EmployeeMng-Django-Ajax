from django.db import models
from django.forms.models import model_to_dict


# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} | {self.location}"
    
    def natural_key(self):
        return model_to_dict(self)

class Employee(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    office = models.ForeignKey(Office, verbose_name=("Office"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fname} {self.lname} | {self.id}"
 
