from django.urls import path
from .views import NewBikeReg, BikeView, BikeUpdate, BikeDelete


urlpatterns = [
    path('',NewBikeReg.as_view(), name='index'),
    path('index',NewBikeReg.as_view(), name='index'),
    path('bikeview',BikeView.as_view(), name='bikeview'),
    path('bikeupdate', BikeUpdate.as_view(), name='bikeupdate'),
    path('bikeupdate/<str:pk>/', BikeUpdate.as_view(), name='bikeupdate'),
    path('bikedelete/<str:pk>/', BikeDelete.as_view(), name='bikedelete'),

]