from django.contrib import admin
from .models import UserAccount, IssueType, DeptNotified, Issue

admin.site.register(UserAccount)
admin.site.register(IssueType)
admin.site.register(DeptNotified)
admin.site.register(Issue)