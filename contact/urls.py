from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'contact_stornco', views.ContactStorncoViewSet)


urlpatterns = [

    # DRF API's URL Router.
    url(r'^', include(router.urls)),

    # DRF API login.
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]