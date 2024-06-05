from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.FloatField()
    engine = models.FloatField()
    transmission = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
