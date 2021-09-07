from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('golfcourse/', views.GolfCourseList.as_view(), name='golfcourse_index'),
    path('golfcourse/<int:pk>/', views.golfcourse_detail, name='golfcourse_detail'),
    path('golfcourse/crate/', views.GolfCourseCreate.as_view(), name='golfcourse_create'),
    path('golfcourse/<int:pk>/update/', views.GolfCourseUpdate.as_view(), name='golfcourse_update')
]
