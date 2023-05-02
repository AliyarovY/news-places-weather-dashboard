import os

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from PIL import Image

NULLABLE = dict(null=True, blank=True)

_PREVIEW_SIZE = (200, 200)


class News(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='media/news/main/')
    preview_image = models.ImageField(
        default='default.jpg',
        upload_to='media/news/preview/',
        **NULLABLE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=now)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title

    def generate_preview_image(self):
        image = Image.open(self.main_image)
        image.thumbnail(_PREVIEW_SIZE, Image.ANTIALIAS)
        preview_path = self.preview_image.path
        if os.path.exists(preview_path):
            os.remove(preview_path)
        image.save(preview_path, 'JPEG', quality=90)
        return self.preview_image

    def save(self, *args, **kwargs):
        self.generate_preview_image()

        super().save(*args, **kwargs)
