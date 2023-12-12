from django.contrib import admin
from .models import UserAccount, IssueType, DeptNotified, Issue
from django_summernote.admin import SummernoteModelAdmin

class TextField(SummernoteModelAdmin):
    summernote_fields = ('issue_content', 'notes_about_notifications')

admin.site.register(UserAccount)
admin.site.register(IssueType)
admin.site.register(DeptNotified)
admin.site.register(Issue)