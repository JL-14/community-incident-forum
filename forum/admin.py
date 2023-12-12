from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserAccount, IssueType, DeptNotified, Issue

@admin.register(Issue, UserAccount, IssueType, DeptNotified)
class TextAdmin(SummernoteModelAdmin):
    summernote_fields = ('issue_content', 'notes_about_notifications')

# admin.site.register(UserAccount)
# admin.site.register(IssueType)
# admin.site.register(DeptNotified)
# admin.site.register(Issue)
