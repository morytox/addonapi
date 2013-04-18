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
		
		# creds_format = {}
		# if addon_name:
		# 	addons = Addon.objects.filter(name=addon_name)
		# 	for addon in addons:
		# 		if len(addon.config_vars):
		# 			name = addon.name
		# 			creds_format[name] = addon.config_vars
		# 	return json.dumps(creds_format, sort_keys=True)
		# else:
		# 	addons = Addon.objects.all()
		# 	for addon in addons:
		# 		if len(addon.config_vars):
		# 			name = addon.name
		# 			creds_format[name] = addon.config_vars
		# 	return json.dumps(creds_format, sort_keys=True)
		if addon_name:
			return Addon.objects.filter(name=addon_name)
		else: 
			return Addon.objects.all()
			