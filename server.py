import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import navi_sound

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(navi_sound.navi_sound,"navi_sound")
server.serve_forever()

