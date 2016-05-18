from django.conf.urls import patterns, include, url


#	blogpost
#	DjangoREST AngularJS
#	http://www.azoft.ru/blog/django-rest-framework/


from rest_framework import routers
from blogpost import views

from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
#router = routers.SimpleRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'blogposts', views.BlogpostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = patterns('',
    url(r'^', views.RootView.as_view()),
)

urlpatterns += [

#urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^blogpost/$', BlogpostViewSet.as_view({'get': 'list'}), name='blog-posts-root'),
    #url(r'^$', views.RootView.as_view()),
    #url(r'^', views.RootView.as_view()),
]