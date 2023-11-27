from django.db import models
from cloudinary.models import CloudinaryField

class User(models.Model):
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=20, unique=True)
    postcode = models.CharField(max_length=8)

class IssueTypes(models.Model):
    ASB = 'ASB'
    ROADS = 'Roads'
    TRAFFIC = 'Traffic'
    PAVEMENTS = 'Pavements'
    PUBLIC_SPACES_MAINTENANCE = 'Public spaces maintenance'
    RUBBISH = 'Rubbish'
    FLY_TIPPING = 'Fly-tipping'

    ISSUE_TYPE_CHOICES = [
        (ASB, 'Anti-social behaviour'),
        (ROADS, 'Road issues'),
        (TRAFFIC, 'Traffic issues'),
        (PAVEMENTS, 'Pavement-related issues'),
        (PUBLIC_SPACES_MAINTENANCE, 'Issues with maintenance of public spaces'),
        (RUBBISH, 'Rubbish-related issues'),
        (FLY_TIPPING, 'Fly-tipping'),
    ]

class Status(models.Model):
    RESOLVED = 'Resolved'
    UNRESOLVED = 'Unresolved'

    STATUS_CHOICES = [
        (RESOLVED, 'Resolved'),
        (UNRESOLVED, 'Not resolved'),
    ]

class Issue(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    type_issue = models.ForeignKey(TypeIssue, on_delete=models.CASCADE, choices=ISSUE_TYPE_CHOICES)
    phone = models.CharField(max_length=7, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date_of_issue = models.DateTimeField(auto_now=False, auto_now_add=False)
    issue_title = models.CharField(max_length=80, blank=False)
    issue_content = models.TextField(max_length=1500)
    issue_location = models.CharField(blank=False)
    image_uploaded = models.BooleanField()
    is_urgent = models.BooleanField()
    dept_notified = models.ManyToManyField(DeptResponsible, blank=True)
    notes_about_notifications = models.TextField(max_length=200)
    status = models.BooleanField(default=UNRESOLVED, choices=STATUS_CHOICES)
