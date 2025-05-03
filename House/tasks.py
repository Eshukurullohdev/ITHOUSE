from celery import shared_task
import time

@shared_task
def process_uploaded_video(video_path):
    time.sleep(10)  # Bu yerda haqiqiy videoni ishlash (FFmpeg, preview, ...)
    return f"Processed video at {video_path}"
