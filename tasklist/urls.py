from stornco.libs.api.routers import NoPutRouter

from . import views

router = NoPutRouter()
router.register(r'task', views.TaskModelViewSet, base_name='task')
urlpatterns = router.urls
