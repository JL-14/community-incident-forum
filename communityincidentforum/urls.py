""" URL configuration for communityincidentforum project. """
from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("forum.urls"), name="forum-urls"),
]

# Error handlers
handler404 = 'communityincidentforum.views.handler404'
handler500 = 'communityincidentforum.views.handler500'
