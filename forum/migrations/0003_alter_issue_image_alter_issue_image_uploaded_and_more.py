# Generated by Django 5.0.1 on 2024-02-21 10:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_issue_image_uploaded_alter_issue_issue_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='image_uploaded',
            field=models.CharField(blank=True, choices=[('Image uploaded', 'Yes'), ('Image not uploaded', 'No')], max_length=18),
        ),
        migrations.AlterField(
            model_name='issue',
            name='notes_about_notifications',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
