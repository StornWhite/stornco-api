# storn.co domain url router
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    # storn.co homepage
    url(r'^$', views.home, name='home'),

    # storn.co admin application
    url(r'^admin/', admin.site.urls),

    # storn.co contact application
    url(r'^contact/', include('contact.urls')),

    # login for django rest framework
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]