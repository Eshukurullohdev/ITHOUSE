from django.db import models
from django.contrib.auth.models import User
class Profesional(models.Model):
    jobs = models.CharField("Kasbi", max_length=100)
    def __str__(self):
        return self.jobs

    class Meta:
        verbose_name = "Kasb"
        verbose_name_plural = "Kasblar"
        ordering = ["jobs"]


class Teacher(models.Model):
    image = models.ImageField(
        "Rasm", 
        upload_to='teachers/', 
        blank=True, 
        null=True, 
        help_text="O‘qituvchi rasmi"
    )
    fullname = models.CharField("To‘liq ism", max_length=100)
    job = models.ForeignKey(
        Profesional, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='teachers',
        verbose_name="Kasbi"
    )

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "O‘qituvchi"
        verbose_name_plural = "O‘qituvchilar"
        ordering = ["fullname"]
        
class VideoUpload(models.Model):
    title = models.CharField(max_length=255)  # Videoga nom
    video_file = models.FileField(upload_to='videos/')  # Video fayl yuklanadi
    poster_video = models.ImageField(upload_to='posters/', blank=True, null=True)  # Video uchun poster
    uploaded_at = models.DateTimeField(auto_now_add=True) 
    
    



class Certificate(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=255)
    file = models.FileField(upload_to='certificates/')
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course}"
    
    
    
    
