# Generated by Django 5.2 on 2025-04-24 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesional',
            options={'ordering': ['jobs'], 'verbose_name': 'Kasb', 'verbose_name_plural': 'Kasblar'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['fullname'], 'verbose_name': 'O‘qituvchi', 'verbose_name_plural': 'O‘qituvchilar'},
        ),
        migrations.AlterField(
            model_name='profesional',
            name='jobs',
            field=models.CharField(max_length=100, verbose_name='Kasbi'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fullname',
            field=models.CharField(max_length=100, verbose_name='To‘liq ism'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, help_text='O‘qituvchi rasmi', null=True, upload_to='teachers/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='House.profesional', verbose_name='Kasbi'),
        ),
    ]
