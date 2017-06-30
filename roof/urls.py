from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'roof', views.RoofModelViewSet)
urlpatterns = router.urls
