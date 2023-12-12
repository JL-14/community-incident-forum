# Generated by Django 4.2.7 on 2023-12-05 18:18

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquirer_email', models.EmailField(max_length=254, verbose_name='Enquirer email address')),
                ('enquirer_phone', models.CharField(blank=True, max_length=12)),
                ('query', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DeptNotified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_notified', models.CharField(choices=[('Reigate and Banstead Council', 'Reigate and Banstead Council'), ('Surrey County Council', 'Surrey County Council'), ('Surrey Police', 'Surrey Police')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(choices=[('ASB', 'Anti-social behaviour'), ('Roads', 'Road issues'), ('Traffic', 'Traffic issues'), ('Pavements', 'Pavement-related issues'), ('Public spaces maintenance', 'Issues with maintenance of public spaces'), ('Rubbish', 'Rubbish-related issues'), ('Fly-tipping', 'Fly-tipping')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('date_of_issue', models.DateTimeField()),
                ('issue_title', models.CharField(max_length=80)),
                ('issue_content', models.TextField(max_length=1500)),
                ('issue_location', models.CharField(max_length=100)),
                ('image_uploaded', models.CharField(choices=[('Image uploaded', 'Image Uploaded'), ('Image not uploaded', 'Image not uploaded')], max_length=18)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('is_urgent', models.CharField(choices=[('Is urgent', 'Needs urgent attention, potential danger'), ('Is not urgent', 'Not an urgent or high risk issue')], max_length=13)),
                ('notes_about_notifications', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('Resolved', 'Resolved'), ('Unresolved', 'Not resolved')], max_length=20)),
                ('approved', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending Review')], max_length=20)),
                ('dept_notified', models.ManyToManyField(blank=True, to='forum.deptnotified')),
                ('issue_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.issuetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(max_length=80)),
                ('comment_content', models.TextField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('comment_approved', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending Review')], max_length=8)),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]