from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import Place

class Admin(ModelAdmin):
    geomap_field_longitude = "id_longitude"
    geomap_field_latitude = "id_latitude"

admin.site.register(Place, Admin)