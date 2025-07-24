from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"


# Car Model model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )
    dealer_id = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
