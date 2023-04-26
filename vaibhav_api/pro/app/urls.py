# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView,MovieApiData,CollectionData,CollectionAPIView
from . import views

from .views import CollectionViewSet
router = DefaultRouter()
router.register(r'collection1', CollectionViewSet)
router.register(r'register', UserRegistrationView),


urlpatterns = [
    path('', include(router.urls)),
    path('movies/', MovieApiData.as_view(), name='MovieApiData'),
    path('collection/', views.CollectionData, name='CollectionData'),
    path('collections/', CollectionAPIView.as_view(), name='CollectionAPIView'),
    path('count/', views.count, name='count'),
    # path('collection/', views.CollectionData, name='CollectionData'),

]



