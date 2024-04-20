from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=80, null=False)
    role = models.CharField(max_length=80, null=False)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.name