from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HelloView

urlpatterns = [
    url(r'^$', HelloView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', HelloView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
