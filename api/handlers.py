from piston.handler import BaseHandler
from addon.models import Addon
import os
import json

class AddonHandler( BaseHandler ):
	allowed_methods = ('GET',)
	model = Addon
	exclude = ('date_created', 'date_modified', 'id')
	# fields = ('name')

	def read( self, request, addon_name=None ):

		if addon_name:
			return Addon.objects.filter(name=addon_name)
		else:
			return Addon.objects.all()