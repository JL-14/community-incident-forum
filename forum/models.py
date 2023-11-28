from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


"""Variables and Tuples for choices/ dropdown menus"""
ASB = 'ASB'
ROADS = 'Roads'
TRAFFIC = 'Traffic'
PAVEMENTS = 'Pavements'
PUBLIC_SPACES_MAINTENANCE = 'Public spaces maintenance'
RUBBISH = 'Rubbish'
FLY_TIPPING = 'Fly-tipping'
ISSUE_TYPE_CHOICES = (
    (ASB, 'Anti-social behaviour'),
    (ROADS, 'Road issues'),
    (TRAFFIC, 'Traffic issues'),
    (PAVEMENTS, 'Pavement-related issues'),
    (PUBLIC_SPACES_MAINTENANCE, 'Issues with maintenance of public spaces'),
    (RUBBISH, 'Rubbish-related issues'),
    (FLY_TIPPING, 'Fly-tipping'),
)

RBC = 'Reigate and Banstead Council'
SCC = 'Surrey County Council'
SP = 'Surrey Police'
DEPARTMENT_CHOICES = (
    (RBC, 'Reigate and Banstead Council'),
    (SCC, 'Surrey County Council'),
    (SP, 'Surrey Police'),
)

APPROVED = 'Approved'
REJECTED = 'Rejected'
PENDING = 'Pending'
APPROVED_CHOICES = (
    (APPROVED, 'Approved'),
    (REJECTED, 'Rejected'),
    (PENDING, 'Pending Review'),
)

RESOLVED = 'Resolved'
UNRESOLVED = 'Unresolved'
STATUS_CHOICES = (
    (RESOLVED, 'Resolved'),
    (UNRESOLVED, 'Not resolved'),
)

"""Models"""
class Username(models.Model):
    """Fields for the Username database module"""
    username = models.EmailField(max_length=100)
    password = models.CharField(max_length=20, unique=True)
    postcode = models.CharField(max_length=8)

class IssueType(models.Model):
    """Fields for the TypeIssue database module with dropdown menu"""
    issue_type = models.CharField(choices=ISSUE_TYPE_CHOICES)

class DeptResponsible(models.Model):
    """Fields for the Department Responsible for the reported issue"""
    department_responsible = models.CharField(choices=DEPARTMENT_CHOICES)
    description = models.CharField(max_length=150)

class Status(models.Model):
    """Fields for the Status database module with dropdown menu"""
    status = models.CharField(choices=STATUS_CHOICES)

class Approved(models.Model):
    """Fields for whether report and comment is approved"""
    approved = models.CharField(choices=APPROVED_CHOICES)

class Issue(models.Model):
    """Fields for Issues and Incidents (Issue) module"""
    username = models.ForeignKey(
        Username,
        on_delete=models.CASCADE
        )
    type_issue = models.ForeignKey(
        IssueType,
        on_delete=models.CASCADE,
        choices=ISSUE_TYPE_CHOICES
        )
    phone = models.CharField(max_length=12, blank=True)
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
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        choices=STATUS_CHOICES
        )
    approved = models.ForeignKey(
        Approved,
        on_delete=models.CASCADE,
        choices=APPROVED_CHOICES
        )

class Comment(models.Model):
    """Fields for the Comment database module"""
    username = models.ForeignKey(Username, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=80, blank=False)
    comment_content = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment_approved = models.ForeignKey(
        Approved,
        on_delete=models.CASCADE,
        choices=APPROVED_CHOICES
        )

class ContactUs(models.Model):
    """Fields for Contacting the developer"""
    email = models.EmailField()
    phone = models.CharField(max_length=12, blank=True)
    query = models.TextField(max_length=500)