from django.urls import path,include
from . import views

urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name='movie-list'),
    path('stream/',views.StreamPlatformAV.as_view(),name='stream-list'),
    path('<int:pk>',views.WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/<int:pk>',views.StreamPlatformDetail.as_view(),name='stream-detail')

   
]
