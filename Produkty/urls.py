from rest_framework import routers
from django.urls import include, path
from .views import ProduktyViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'produkty', ProduktyViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index),
]