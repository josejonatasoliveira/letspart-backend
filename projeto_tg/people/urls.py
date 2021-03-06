from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^profile/(?P<username>[^/]*)/$",
        views.profile_detail, name="profile_detail"),
    url(r"^edit/$", views.profile_edit, name="profile_edit"),
]
