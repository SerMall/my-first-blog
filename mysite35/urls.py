"""mysite35 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
"""
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index' ),
)
"""
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index' ),
]


#	Приклад з http://djbook.ru/rel1.4/intro/tutorial03.html
#	"Упрощаем конфигурацию URL-ов"

#	polls
#	Приклад з http://djbook.ru/rel1.4/intro/tutorial03.html
#	"Разъединение конфигурации URL-ов"
#	Скопируйте mysite/urls.py в polls/urls.py. 
#	Измените mysite/urls.py удалив URL-шаблоны приложения и замените их на include():

from django.contrib import admin
admin.autodiscover()
"""
urlpatterns += patterns('',
#urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
"""
urlpatterns += [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

#	rest1
#	Django REST
#	http://www.django-rest-framework.org/tutorial/quickstart/
#	"URL"
"""
urlpatterns += patterns('',
    url(r'^rest1/', include('rest1.urls')),
)
"""
urlpatterns += [
    url(r'^rest1/', include('rest1.urls')),
]

#	blogpost
#	DjangoREST AngularJS
#	http://www.azoft.ru/blog/django-rest-framework/

#urlpatterns += patterns('',
#    url(r'^blogpost/', include('blogpost.urls')),
#)

urlpatterns += [
    url(r'^blogpost/', include('blogpost.urls')),
]

