from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('stream',views.StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/',views.WatchListAV.as_view(),name='movie-list'),
    # path('stream/',views.StreamPlatformAV.as_view(),name='stream-list'),
    path('<int:pk>',views.WatchDetailAV.as_view(),name='movie-detail'),
    path('',include(router.urls)),
    # path('stream/<int:pk>',views.StreamPlatformDetail.as_view(),name='streamplatform-detail'),
    # path('review/',views.ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail')
    path('<int:pk>/review',views.ReviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create',views.ReviewCreate.as_view(),name='review-create'),
    path('review/<int:pk>',views.ReviewDetail.as_view(),name='review-detail')
   
]
