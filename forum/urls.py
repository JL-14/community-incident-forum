from django.urls import path, include
from . import views
from .views import IssueList, landing_page, report_detail, comment_edit, comment_delete, contact

urlpatterns = [
    path("", landing_page, name="home"),
    path("reportlist/", views.IssueList.as_view(), name="reportlist"),
    path("contact/", views.contact, name="contact"),
    path("<slug:slug>/", views.report_detail, name="report-detail"),
    path(
        '<slug:slug>/comment_edit/<int:comment_id>', 
        views.comment_edit, 
        name='comment_edit'
    ),
    path(
        '<slug:slug>/comment_delete/<int:comment_id>',
        views.comment_delete, 
        name='comment_delete'
    ),
]
