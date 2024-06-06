from django.urls import path 
from . import views

urlpatterns =[
    path('student/list',views.StudentListApiView.as_view(), name='student-list'),
    path('student/create',views.StudentCreateApiView.as_view(), name='student-create'),
    path('student/<pk>/update',views.StudentUpdateApiView.as_view(), name='student-update'),
    path('student/<pk>/delete',views.StudentDeleteApiView.as_view(), name='student-delete'),
]