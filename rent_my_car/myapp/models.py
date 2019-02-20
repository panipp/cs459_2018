from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    tel = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Car(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    purchasing_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"{self.brand} {self.name}"

class Rent(models.Model):
    start = models.DateField()
    stop = models.DateField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
