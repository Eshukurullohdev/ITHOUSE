from django.contrib import admin
from House.models import *
admin.site.register(Profesional)
admin.site.register(Teacher)
@admin.register(VideoUpload)
class VideoUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')