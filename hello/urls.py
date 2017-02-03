from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'hello', views.HelloModelViewSet)
urlpatterns = router.urls
