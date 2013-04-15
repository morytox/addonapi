from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import AddonHandler

# class CsrfExemptResource( Resource ):
#     def __init__( self, handler, authentication = None ):
#         super( CsrfExemptResource, self ).__init__( handler, authentication )
#         self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

addon_resource = Resource( AddonHandler )

urlpatterns = patterns( '',
    url( r'^addonapi/$', addon_resource )
)