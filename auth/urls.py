from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('auth.views',
    url(r'^login', 'login'),
    url(r'^logout', 'logout'),
    url(r'^newUser', 'newUser'),
)
