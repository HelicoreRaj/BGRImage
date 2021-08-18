from django.urls import include,path,re_path
from rest_framework import routers
from .views import TestView

urlpatterns = [
	path('test/',TestView.as_view(), name='test'),
]