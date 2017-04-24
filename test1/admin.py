from django.contrib import admin

# Register your models here.
from .models import ImageUpload

class ImageUploadAdmin(admin.ModelAdmin):
	list_display = ('image',)

admin.site.register(ImageUpload, ImageUploadAdmin)