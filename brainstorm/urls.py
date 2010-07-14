from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'bsnet.brainstorm.views.index'),
	(r'^(?P<topic_id>\d+)/$', 'bsnet.brainstorm.views.details'),
)
