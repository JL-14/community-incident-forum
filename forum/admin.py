from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserAccount, DeptNotified, Issue

@admin.register(Issue)
class TextAdmin(SummernoteModelAdmin):
    """Using Summernote formatting for admin page"""
    list_filter = ('issue_type', 'date_of_issue', 'status')
    summernote_fields = ('issue_content', 'notes_about_notifications')

admin.site.register(UserAccount)
admin.site.register(DeptNotified)
