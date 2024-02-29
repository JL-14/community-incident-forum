from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserAccount, DeptNotified, Issue

admin.site.register(Issue)
admin.site.register(UserAccount)
admin.site.register(DeptNotified)
