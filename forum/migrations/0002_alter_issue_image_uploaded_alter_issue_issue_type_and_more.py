# Generated by Django 4.2.7 on 2023-12-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='image_uploaded',
            field=models.CharField(choices=[('Image uploaded', 'Yes'), ('Image not uploaded', 'No')], max_length=18),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.CharField(choices=[('ASB', 'Anti-social behaviour'), ('Roads', 'Road issues'), ('Traffic', 'Traffic issues'), ('Pavements', 'Pavement-related issues'), ('Public spaces maintenance', 'Issues with maintenance of public spaces'), ('Rubbish', 'Rubbish-related issues'), ('Fly-tipping', 'Fly-tipping')], max_length=50),
        ),
        migrations.DeleteModel(
            name='IssueType',
        ),
    ]