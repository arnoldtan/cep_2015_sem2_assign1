from django.conf.urls import patterns, include, url
from django.contrib import admin
from stats import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lgbtstats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^country/(?P<country_name>[\w\s]{0,200})$', views.country, name='country'),
    
    url(r'^topic/(?P<topic_name>[\w\s]{0,200})$', views.topic, name='topic'),
)
