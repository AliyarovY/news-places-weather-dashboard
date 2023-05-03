from django.urls import path

from .views import WeatherXLSExportAPIView

urlpatterns = [
    path('weather_xls_export', WeatherXLSExportAPIView.as_view()),
]
