import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://192.168.76.24:8000/")
proxy.navi_sound()
