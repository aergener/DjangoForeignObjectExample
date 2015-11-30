from django.conf.urls import include, url
from django.contrib import admin

from app import urls as app_urls

urlpatterns = [
    url(r'^', include(app_urls)),
]
