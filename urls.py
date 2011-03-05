from django.conf.urls.defaults import *
#api
from piston.resource import Resource
from django_12urenloop.drbreaker.handlers import LapHandler

#csrf workaround
class CsrfExemptResource(Resource):
            """A Custom Resource that is csrf exempt"""
            def __init__(self, handler, authentication=None):
                super(CsrfExemptResource, self).__init__(handler, authentication)
                self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)
 
lap_handler = CsrfExemptResource(LapHandler)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_12urenloop/', include('django_12urenloop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^score/','drbreaker.views.scores'),
    (r'^api/', lap_handler)
)
