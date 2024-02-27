# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("forum/", views.IssueList.as_view(), name="home"),
]