from django.db import models


# Create your models here.
class Apartment(models.Model):
    equipped = models.BooleanField
    bedrooms = models.IntegerField
    living_rom = models.IntegerField
    bathroom = models.IntegerField
    price = models.IntegerField
    features = models.CharField(max_length=1000)  # fridge gas_stove balcony water_heater dish_washer washing_machine
    # surveillance_camera cooking_tools oven
    description = models.CharField(max_length=1000)
