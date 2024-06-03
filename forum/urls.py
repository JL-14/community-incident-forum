# from django.contrib import admin
from django.urls import path, include
from . import views
from .views import IssueList, landing_page, report_detail, comment_edit, comment_delete

urlpatterns = [
    path("", landing_page, name="home"),
    path("reportlist/", views.IssueList.as_view(), name="reportlist"),
    path("<slug:slug>/", views.report_detail, name="report-detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>', 
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]