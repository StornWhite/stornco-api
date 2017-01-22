# storn.co domain url router
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # storn.co homepage
    url(r'^$', views.home, name='home'),

    # storn.co admin application
    url(r'^admin/', admin.site.urls),
]
