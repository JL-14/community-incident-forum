# Generated by Django 5.0.1 on 2024-02-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_issue_issue_type_issue_slug_alter_issue_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
