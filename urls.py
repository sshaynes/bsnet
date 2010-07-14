from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^brainstorms/', include('bsnet.brainstorm.urls')),
	(r'^admin/', include('admin.site.urls')),
)
