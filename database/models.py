from datetime import datetime
from tkinter.tix import Tree
from unicodedata import name
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils import timezone, formats
import pytz
import datetime
import os

    # indonesia_tz = pytz.timezone('Asia/Jakarta')
    # time = timezone.localtime(waktu_update)
    # time.strftime("%d %B %Y %H:%M:%S")
class PostModel(models.Model):
    gambar = models.ImageField(upload_to='', null = True, blank = False)
    waktu = models.DateTimeField(auto_now_add=True)
    waktu_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def waktu_indonesia(self):
        waktu_indo = timezone.localtime(self.waktu, pytz.timezone('Asia/Jakarta'))
        return waktu_indo.strftime("%d %B %Y %H:%M WIB")
    
    def waktu_update_indonesia(self):
        waktu_update_indo = timezone.localtime(self.waktu_update, pytz.timezone('Asia/Jakarta'))
        return waktu_update_indo.strftime("%d %B %Y %H:%M WIB")
    
    LIST_CATEGORY = (
        ('Pneumonia', 'Pneumonia'),
        ('Tuberculosis', 'Tuberculosis'),
        ('COVID19', 'COVID19'),
        ('Normal', 'Normal'),
    )

    category = models.CharField(
        max_length=100,
        choices=LIST_CATEGORY,blank=False
    )

    def save(self):
        self.slug = slugify(self.gambar)
        super(PostModel, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.gambar)

