from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'addonapi.views.home', name='home'),
#     # url(r'^addonapi/', include('addonapi.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )
admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/', include('api.urls', namespace="api")),
    (r'^addons/', include('addon.urls', namespace="addon")),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
	(r'^static/(.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT
	}),
)