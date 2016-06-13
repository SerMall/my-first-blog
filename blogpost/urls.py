from django.conf.urls import patterns, include, url


from rest_framework import routers
from blogpost import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'blogposts', views.BlogpostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='blogpost/index.html'), name='index' ),
]

urlpatterns += [
    url(r'^', include(router.urls)),
]


