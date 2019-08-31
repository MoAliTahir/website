from django.urls import path
from . import views

urlpatterns = [
    # /stackhome/
    path('', views.stackhome, name='index'),

    # /music/id
    #path('<int:album_id>/', views.detail, name='detail'),
]