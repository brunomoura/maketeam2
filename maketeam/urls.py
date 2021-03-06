from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', direct_to_template, {
    #     'template': 'home.html'
    # }, name='home'),
    url(r'^$', 'app.views.time', name='time'),
    url(r'^(?P<fanpage_id>\d+)/$', 'app.views.time', name='time_fanpage'),
    url(r'^compartilhar', 'app.views.compartilhar', name='compartilhar'),
    # url(r'^maketeam/', include('maketeam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fandjango/', include('fandjango.urls')),
)
