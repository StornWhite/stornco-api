# storn.co domain url router
from django.conf.urls import url, include
from django.contrib import admin

from . import views
from contact import urls as contact_urls


# API routers for each application:
v1_api_routers = [

    url(r'^contact-stornco/', include(contact_urls) ),

]

# Main URL Patterns
urlpatterns = [

    # storn.co homepage
    url(r'^$', views.home, name='home'),

    # hello
    url(r'^api/v1/', include(v1_api_routers)),

    # login for django rest framework
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    # storn.co admin application
    url(r'^admin/', admin.site.urls),

]