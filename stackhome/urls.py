from django.urls import path

from . import views

app_name = "stackhome"
urlpatterns = [
    # /stackhome/
    # path('', views.stackhome, name='index'),

    #/stackhome/id
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]