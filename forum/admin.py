from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserAccount, DeptNotified, Issue, Comment
from .forms import AdminCommentForm


@admin.register(Issue)
class IssueDetails(SummernoteModelAdmin):
    list_display = (
        'issue_title', 'approved', 'date_of_issue', 
        'issue_location', 'user', 'created_on',
    )
    search_fields = ['issue_title', 'issue_content', 'issue_location']
    list_filter = ('date_of_issue', 'approved', 'status', 'issue_type')
    prepopulated_fields = {'slug': ('issue_title',)}
    summernote_fields = ('issue_content',)


admin.site.register(UserAccount)
admin.site.register(DeptNotified)


class CommentAdmin(admin.ModelAdmin):
    form = AdminCommentForm
    list_display = (
        'approved', 'comment_author', 
        'comment_issue_title', 'created_on',
    )
    list_filter = ('approved', 'created_on')
    search_fields = ('comment_content', 'comment_author__username')

    def comment_issue_title(self, obj):
        return obj.comment_issue.issue_title

    comment_issue_title.short_description = 'Issue Title'


admin.site.register(Comment, CommentAdmin)
