from django.db import models

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