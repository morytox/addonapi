from piston.handler import BaseHandler

class AddonHandler( BaseHandler ):
    def read( self, request, expression ):
        return eval( expression )