from django.views.generic import ListView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from stats import views
from stats.models import Country

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lgbtstats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^country/all/$', ListView.as_view(
        template_name="country/country_list.html",
        context_object_name="countries_list",
        model=Country
    )),
    url(r'^country/add/$',
        views.CountryCreate.as_view(
            template_name="country/country_form.html",
            success_url="/country/all/"),
        ),
    url(r'^country/edit/(?P<pk>\d+)$',
        views.CountryUpdate.as_view(
            template_name="country/country_form.html",
            success_url="/country/all/"),
        ),
    url(r'^country/delete/(?P<pk>\d+)$',
        views.CountryDelete.as_view(
            template_name="country/country_delete.html",
            success_url="/country/all/"),
    ),
    
    url(r'^api/country/all/$', views.ApiCountryAll.as_view()),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^country/(?P<country_name>[\w\s]{0,200})$', views.CountryView.as_view(), name='country'),
    url(r'^topic/(?P<topic_name>[\w\s]{0,200})$', views.TopicView.as_view(), name='topic'),
)
