from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserAccount, DeptNotified, Issue, Comment

@admin.register(Issue)
class IssueDetails(SummernoteModelAdmin):

    list_display = ('issue_title', 'slug', 'approved', 'date_of_issue', 'issue_location', 'user', 'created_on',)
    search_fields = ['issue_title', 'issue_content', 'issue_location']
    list_filter = ('date_of_issue', 'approved', 'status', 'issue_type')
    prepopulated_fields = {'slug':('issue_title',)}
    summernote_fields = ('issue_content',)

admin.site.register(UserAccount)
admin.site.register(DeptNotified)

admin.site.register(Comment)
