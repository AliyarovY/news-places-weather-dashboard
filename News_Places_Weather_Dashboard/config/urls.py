from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('news.urls')),
    path('api/', include('place.urls')),
    path('api/', include('weather_summary_.urls')),

    path('summernote/', include('django_summernote.urls')),

    path('', include('swagger.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
