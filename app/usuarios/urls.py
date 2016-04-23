
from django.conf.urls import url
from .views import usuarios

urlpatterns = [

    url(r'^usuarios/$', usuarios, name='usuarios')

]
