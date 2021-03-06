from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest1 import views
#from rest1.views import UserViewSet, GroupViewSet
router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#	Розводка свій API за допомогою автоматичної маршрутизації URL.
#	Крім того, ми включаємо URL для входу для проглядається API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

