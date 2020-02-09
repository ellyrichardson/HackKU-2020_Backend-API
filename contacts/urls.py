from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactsViewSet, basename='contactsapiview')
router.register(r'sms', views.SMSViewSet, basename='smsapiview')

urlpatterns = [
    path('api/', include(router.urls)),
]
