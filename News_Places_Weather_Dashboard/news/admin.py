from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import News


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(News, NewsAdmin)
