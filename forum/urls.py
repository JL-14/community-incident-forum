# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IssueList.as_view(), name="home"),
    path("<slug:slug>/", views.report_detail, name="report-detail"),
]