from rest_framework import routers
from address.views import AddressViewSet
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'addresses', AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]