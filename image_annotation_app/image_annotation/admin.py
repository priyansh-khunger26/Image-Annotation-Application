from django.contrib import admin
from .models import AnnotatedImage
# from .models import Image

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('class_name', 'status', 'image')

@admin.register(AnnotatedImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','class_name', 'status', 'image')
