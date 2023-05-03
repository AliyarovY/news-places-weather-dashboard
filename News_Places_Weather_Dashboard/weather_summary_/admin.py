from django.contrib import admin
from .models import WeatherSummary

class WeatherSummaryAdmin(admin.ModelAdmin):
    list_display = ('place', 'temperature', 'humidity', 'pressure', 'wind_direction', 'wind_speed', 'created_at')
    list_filter = ('place', 'created_at')

admin.site.register(WeatherSummary, WeatherSummaryAdmin)


