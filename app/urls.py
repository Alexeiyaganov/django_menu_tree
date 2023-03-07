from django.urls import path

from django.urls import re_path as url, path
from .views import IndexView

app_name = 'app'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^\w*$', IndexView.as_view(), name='index'),
    path('hhh/', IndexView.as_view(), name='index'),

]