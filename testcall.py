import urllib2

opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://127.0.0.1:8000/api/',data='{"mac":"01:23:45:67:89:ab"}')
request.add_header('Content-Type', 'application/json')
request.get_method = lambda: 'PUT'
url = opener.open(request)
print url.read()
