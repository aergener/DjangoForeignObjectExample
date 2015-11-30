from django.conf.urls import url
from app import views as app_views

urlpatterns = [
    url(r'^stock/$', app_views.StockListView.as_view()),
]
