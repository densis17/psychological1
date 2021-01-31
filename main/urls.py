from django.urls import path
from django.conf.urls import url
from . import views
from .views import update_counter


urlpatterns = [
    path('', views.main, name='main'),
    path('anketa', views.anketa, name='anketa'),
    path('test', views.test, name='test'),
    url(r'^update_counter/', update_counter),
]
