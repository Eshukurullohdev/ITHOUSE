from django.db import models



class profesional(models.Model):
    jobs = models.CharField(max_length=100)
    
    def __str__(self):
        return self.jobs

class Teacher(models.Model):
    image = models.ImageField(upload_to='teachers/')
    fullname = models.CharField(max_length=100)
    job = models.ForeignKey(profesional, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = "O‘qituvchi"
        verbose_name_plural = "O‘qituvchilar"
    

