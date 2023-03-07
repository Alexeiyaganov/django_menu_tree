from django.urls import path

from django.urls import re_path
from .views import IndexView


urlpatterns = [
    re_path('hhh', IndexView.as_view(), name='index'),
    re_path('.*/', IndexView.as_view(), name='index'),
]