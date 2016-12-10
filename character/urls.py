# character/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^(?P<character_id>[0-9]+)/$', views.detail, name='detail'),
]
