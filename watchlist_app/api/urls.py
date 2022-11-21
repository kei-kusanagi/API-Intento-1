from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views

router = DefaultRouter()
router.register('stream', views.StreamPlataformVS, basename='streamplataform')

urlpatterns = [
    path('', include(router.urls)),
]