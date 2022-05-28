from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path("crawl_TGDD",views.crawl_TGDD),

]