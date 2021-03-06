from django.conf.urls import *
from . import views
# class CsrfExemptResource( Resource ):
#     def __init__( self, handler, authentication = None ):
#         super( CsrfExemptResource, self ).__init__( handler, authentication )
#         self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )
urlpatterns = patterns(
    '',
    url(r'^update/$', views.Update, name='index'),
    url(r'^$', views.AddonListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.AddonDetailView.as_view(), name='detail')
)
