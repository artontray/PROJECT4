from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.TestnetList.as_view(), name="home"),
]
