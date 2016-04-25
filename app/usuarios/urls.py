
from django.conf.urls import include, url
from rest_framework import routers
from .views import usuarios, UsuarioViewSet
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)


urlpatterns = [

    url(r'^usuarios/$', usuarios, name='usuarios'),
    url(r'^api-rest/', include(router.urls)),
]
