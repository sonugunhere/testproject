from django.db import models


class Bike(models.Model):
    owner_name = models.CharField(max_length=200, default=True)
    bike_name = models.CharField(max_length=200)
    reg_number = models.OneToOneField('BikeReg', on_delete=models.CASCADE)


    def __str__(self):
        return self.owner_name+" "+self.bike_name+" "+self.reg_number.reg_number


class BikeReg(models.Model):
    reg_number = models.CharField(max_length=200)


    def __str__(self):
        return self.reg_number
