from django.urls import path
from django.urls import path
from . import serializers, views
urlpatterns = [
    path('', views.api),
    path('student/', serializers.StudentList.as_view()),
    path('student/<str:pk>', serializers.StudentDetail.as_view()),

]
