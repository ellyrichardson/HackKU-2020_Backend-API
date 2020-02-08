from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'status', views.StatusAPIViewSet, basename='statusapiview')
router.register(r'onoff', views.OnOffAPIViewSet, basename='onoffendpoint')
router.register(r'clearsensordata', views.ClearSensorDataViewSet, basename='cleardatasensor')

urlpatterns = [
    path('api/', include(router.urls)),
]
