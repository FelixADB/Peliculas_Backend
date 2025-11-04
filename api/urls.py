from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneroViewSet, PeliculaViewSet

router = DefaultRouter()
router.register(r'generos', GeneroViewSet)
router.register(r'peliculas', PeliculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]