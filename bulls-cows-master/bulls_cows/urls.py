from django.contrib import admin
from django.urls import include, path

from bulls_cows.views.home import home, about
from bulls_cows.views.play import Play

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path("", home, name="home"),
    path("play/", Play.as_view(), name="play"),
    path("about/", about, name="about"),
]

