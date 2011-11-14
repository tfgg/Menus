from django.views.static import serve
from django.conf.urls.defaults import patterns, include, url

from settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'menus.views.home', name='home'),
    url(r'^', include('Menus.core.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', serve,
     {'document_root': MEDIA_ROOT,
      'show_indexes': True}),
)
