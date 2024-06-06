from django.urls import path 
from . import views


urlpatterns =[
    path("register", views.RegisterApiview.as_view(), name='register'),
    path("register/<pk>/update", views.RegisterUpdateApiView.as_view(), name='register-update'),
    path("login", views.LoginApiView.as_view(), name='login'),
]