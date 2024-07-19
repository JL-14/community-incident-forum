""" Python models for app """
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Variables and tuples for choices/dropdown menus
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

IS_URGENT = 'Is urgent'
IS_NOT_URGENT = 'Is not urgent'
URGENT_CHOICES = (
    (IS_URGENT, 'Needs urgent attention, potential danger'),
    (IS_NOT_URGENT, 'Not an urgent or high risk issue'),
)


class UserAccount(models.Model):
    """Fields for the User Account database module"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=8)


class DeptNotified(models.Model):
    """Fields for the Department Responsible for the reported issue"""
    dept_notified = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return str(self.dept_notified) if self.dept_notified else "No Dept Notified"


class Issue(models.Model):
    """Fields for Issues and Incidents (Issue) module"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date_of_issue = models.DateTimeField()
    issue_title = models.CharField(max_length=80, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    issue_content = models.TextField(max_length=1500)
    issue_location = models.CharField(max_length=100, blank=False)
    is_urgent = models.CharField(max_length=13, choices=URGENT_CHOICES)
    featured_image = CloudinaryField('image', default='placeholder')
    dept_notified = models.ManyToManyField(DeptNotified, blank=True)
    notes_about_notifications = models.TextField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    approved = models.CharField(max_length=20, choices=APPROVED_CHOICES)

    def __str__(self):
        return str(self.issue_title) if self.issue_title else "No title"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.issue_title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    """ Fields for Comment module """
    comment_issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="comments", null=False, blank=False
    )
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    comment_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Meta settings for comment view """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_content} by {self.comment_author}"
