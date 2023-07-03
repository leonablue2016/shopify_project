from django.urls import path
from .views import (
    PictureListView,
    PictureDetailView,
    PictureCreateView,
    PictureUpdateView,
    PictureDeleteView,
    buyPicture
)
from . import views

urlpatterns = [
    path('search/', PictureListView.as_view(), name='pic-search'),
    path('new/', PictureCreateView.as_view(), name='pic-create'),
    path('<int:pk>/update/', PictureUpdateView.as_view(), name='pic-update'),
    path('<int:pk>/delete/', PictureDeleteView.as_view(), name='pic-delete'),
    path('all/',views.allPictures, name = 'pictures'),
    path('<int:pk>/',PictureDetailView.as_view(), name = 'pic-detail'),
    path('<int:pk>/buy/', views.buyPicture, name = 'buy-pic')
    
]