from django.urls import path, include
from . import views
urlpatterns = [
        path('index',views.main,name='main'),
]
