from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('main.views',
	url(r'^new_goal/', 'new_goal'),
	url(r'',    'home'),
	
)

