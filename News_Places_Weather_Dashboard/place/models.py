from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_admin_geomap import GeoItem


class Place(models.Model, GeoItem):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=90, decimal_places=60)
    longitude = models.DecimalField(max_digits=90, decimal_places=60)
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MinValueValidator(0),
                                     MaxValueValidator(25),
                                 ])

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    class Meta:
        db_table = 'place'
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return self.name
