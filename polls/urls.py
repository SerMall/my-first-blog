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

"""
#	Приклад з http://djbook.ru/rel1.4/intro/tutorial03.html
#	"Разъединение конфигурации URL-ов"

from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
"""


#	=============================================================
#	Приклад з http://djbook.ru/rel1.4/intro/tutorial04.html
#	"Общие представления: меньше кода - меньше проблем"

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

#urlpatterns = patterns('',
urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
]
#)

#	Теперь вы можете удалить функции index(), detail() и results() из polls/views.py. 
#	Они нам больше не нужны.
#	return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

