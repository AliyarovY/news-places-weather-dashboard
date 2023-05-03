import os
from pathlib import Path

from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.utils.timezone import now
from PIL import Image

NULLABLE = dict(null=True, blank=True)

_PREVIEW_SIZE = 200

_PREVIEW_PATH = os.path.join(settings.MEDIA_ROOT, 'news/previews/')

_MAIN_IMG_PATH = os.path.join(settings.MEDIA_ROOT, 'news/main/')


class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    main_image = models.ImageField(upload_to='news/main/', **NULLABLE)
    preview_image = models.ImageField(upload_to='news/previews/', **NULLABLE)
    text = models.TextField(unique=True)
    pub_date = models.DateTimeField(default=now)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title

    def _copy_main_image(self):
        if not os.path.exists(_PREVIEW_PATH):
            path = Path(_PREVIEW_PATH)
            path.mkdir(exist_ok=True)

        main_img_name = self.main_image.name.split('/')[-1]
        main_img_path = os.path.join(_MAIN_IMG_PATH, main_img_name)
        with open(main_img_path, 'rb') as mn_file:
            main_img = mn_file.read()

            pr_img_path = os.path.join(_PREVIEW_PATH, main_img_name)
            with open(pr_img_path, 'wb') as pr_file:
                pr_file.write(main_img)
                return pr_img_path

    def generate_preview_image(self):
        if not self.preview_image:
            self.preview_image = self._copy_main_image()

        with Image.open(self.preview_image) as img:
            width, height = img.size
            min_size = min(width, height)
            factor = _PREVIEW_SIZE / min_size
            img = img.resize((int(width * factor), int(height * factor)))
            img.save(self.preview_image.path, format='JPEG')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.main_image:
            self.generate_preview_image()
