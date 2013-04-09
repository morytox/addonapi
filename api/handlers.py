from piston.handler import BaseHandler

class AddonHandler( BaseHandler ):
    def read( self, request, expression ):
    	cred_file = open(os.environ["CRED_FILE"])
     	data = json.load(cred_file)
        return data