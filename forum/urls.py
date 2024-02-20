from django.urls import path
from . import views

urlpatterns = [
    path('', views.IssueList.as_view(), name='home'),
]