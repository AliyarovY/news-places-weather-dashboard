from django.db import models


class WeatherSummary(models.Model):
    place = models.ForeignKey('place.Place', on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.DecimalField(max_digits=5, decimal_places=2)
    wind_direction = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'weather_summary'
        ordering = ['-created_at']
        verbose_name_plural = 'Weather summaries'
