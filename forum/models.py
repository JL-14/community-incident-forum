from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


#Variables and Tuples for choices/ dropdown menus
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

IMAGE_UPLOADED = 'Image uploaded'
IMAGE_NOT_UPLOADED = 'Image not uploaded'
IMAGE_UPLOAD_CHOICES = (
    (IMAGE_UPLOADED, 'Yes'),
    (IMAGE_NOT_UPLOADED, 'No'),
)

IS_URGENT = 'Is urgent'
IS_NOT_URGENT = 'Is not urgent'
URGENT_CHOICES = (
    (IS_URGENT, 'Needs urgent attention, potential danger'),
    (IS_NOT_URGENT, 'Not an urgent or high risk issue')
)

"""Models"""
class UserAccount(models.Model):
    """Fields for the User Account database module"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=8)

class DeptNotified(models.Model):
    """Fields for the Department Responsible for the reported issue"""
    dept_notified = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

class Issue(models.Model):
    """Fields for Issues and Incidents (Issue) module"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPE_CHOICES)
    phone = models.CharField(max_length=12, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date_of_issue = models.DateTimeField()
    issue_title = models.CharField(max_length=80, blank=False)
    issue_content = models.TextField(max_length=1500)
    issue_location = models.CharField(max_length=100, blank=False)
    image_uploaded = models.CharField(
        max_length=18,
        choices=IMAGE_UPLOAD_CHOICES,
        blank=True
        )
    image = CloudinaryField('image', blank=True)
    is_urgent = models.CharField(
        max_length=13,
        choices=URGENT_CHOICES
        )
    dept_notified = models.ManyToManyField(DeptNotified, blank=True)
    notes_about_notifications = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    approved = models.CharField(max_length=20, choices=APPROVED_CHOICES)

class Comment(models.Model):
    """Fields for the Comment database module"""
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=80, blank=False)
    comment_content = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment_approved = models.CharField(
        max_length=8,
        choices=APPROVED_CHOICES
        )

class ContactUs(models.Model):
    """Fields for Contacting the developer"""
    enquirer_email = models.EmailField(verbose_name='Enquirer email address')
    enquirer_phone = models.CharField(max_length=12, blank=True)
    query = models.TextField(max_length=500)