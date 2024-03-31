from django.urls import path, re_path
from . import views

urlpatterns = [
  path('urls/create', views.UrlShortenerView.as_view()),
  re_path(r'^.*$', views.RedirectorView.as_view())
]