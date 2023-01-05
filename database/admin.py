from django.contrib import admin

# Register your models here.
from .models import PostModel


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]

admin.site.register(PostModel, PostAdmin)