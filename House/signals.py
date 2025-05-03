from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VideoUpload
from .tasks import process_uploaded_video

@receiver(post_save, sender=VideoUpload)
def handle_video_upload(sender, instance, created, **kwargs):
    if created:
        process_uploaded_video.delay(instance.video_file.path)
        # process_uploaded_video.delay(instance.video_file.path)  # Celery vazifasini chaqirish