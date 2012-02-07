from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^today$', views.today, name="today"),
    url(r'^rate/(?P<meal_id>.*)/(?P<rating>.*)$', views.rate, name="rate_meal"),
)

