from piston.handler import BaseHandler
import os
import json

class AddonHandler( BaseHandler ):

    def read( self, request ):
    	cred_file = open(os.environ["CRED_FILE"])
     	data = json.load(cred_file)
        return cred_file