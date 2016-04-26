
from django.conf.urls import include, url
from rest_framework import routers
from .views import usuarios, UsuarioViewSet, login
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)


urlpatterns = [

    url(r'^usuarios/$', usuarios, name='usuarios'),
    url(r'^login/$', login, name='login'),
    url(r'^api-rest/', include(router.urls)),
]
