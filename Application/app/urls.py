from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# default router automatically creates the yrl patterns for CRUD opertaions

#  register the viewsets
# r is for raw strings this counts '\' as part of string and not as escape char
router.register(r'androidapps', views.AndriodAppViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'tasks', views.TaskViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
