# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IssueList.as_view(), name="home"),
    path("<slug:slug>/", views.report_detail, name="report-detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]