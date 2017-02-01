# storn.co domain url router
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from . import views
from contact import urls as contact_urls


# API routers for each application:
v1_api_routers = [

    url(r'^contact-stornco/', include(contact_urls) ),

]

# Main URL Patterns
urlpatterns = [

    # django rest frame work routes
    url(r'^api/v1/', include(v1_api_routers)),

    # logins for django rest framework
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    # storn.co admin application
    url(r'^admin/', admin.site.urls),

]

# Add swagger API documentation
schema_view = get_swagger_view(title='StornCo API')
urlpatterns += (url(r'^$', schema_view),)
