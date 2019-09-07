from django.db import models


# Create your models here.
class Apartment(models.Model):
    NUMBERS = (
        (0, 'zero'),
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
    )
    address = models.CharField(max_length=1000, default="null")
    equipped = models.BooleanField(default=False)
    bedrooms = models.IntegerField(choices=NUMBERS)
    living_rom = models.IntegerField(choices=NUMBERS)
    bathroom = models.IntegerField(choices=NUMBERS, default=1)
    price = models.PositiveSmallIntegerField(default=0)
    features = models.CharField(max_length=1000)  # fridge gas_stove balcony water_heater dish_washer washing_machine
    # surveillance_camera cooking_tools oven
    description = models.CharField(max_length=1000)
    available = models.BooleanField(default=True)
