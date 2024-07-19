""" URL paths for use in the app """

from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="home"),
    path("reportlist/", views.IssueList.as_view(), name="reportlist"),
    path("contact/", views.contact, name="contact"),
    path("<slug:slug>/", views.report_detail, name="report-detail"),
    path("<slug:slug>/add_comment/", views.add_comment,
        name="add_comment"),
    path("<slug:slug>/edit_comment/<int:comment_id>/",
        views.comment_edit, name='comment_edit'),
    path("<slug:slug>/delete_comment/<int:comment_id>/",
        views.comment_delete,
        name='comment_delete'),
]

# Error handlers
handler404 = 'forum.views.handler404'
handler500 = 'forum.views.handler500'
