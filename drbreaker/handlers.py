from drbreaker.models import Team
#api's met piston
from piston.handler import BaseHandler
import piston

class LapHandler(BaseHandler):
	allowed_methods = ('POST','PUT','GET',)
	model = Team


	def read(self, request):
		"""
		Returns a single post if `blogpost_id` is given,
		otherwise a subset.

		"""
		base = Team.objects
		return base.all() # Or base.filter(...)

	def create(self,request,post_slug):
		""" 
			creates initial configuration, put hardcoded teams here
		"""
		if post_slug  =="bootstrap":
			if Team.objects:
				return "DB not empty"
				output = piston.utils.rc.DUPLICATE_ENTRY
				output.write ("DB not empty!")
				return output
			else:
				#create hardcoded teams here
				return piston.utils.rc.ALL_OK    #piston.utils.rc.CREATED

	def update(self,request,*args, **kwargs):

		if request.content_type:

			         		
			data = request.data
            		mac = data['mac']
			team = Team.objects.filter(macAddress=mac)[0]
			team.score = team.score +1
			team.save()
			return piston.utils.rc.ALL_OK   

		else:
			print "bad request"
			return piston.utils.rc.BAD_REQUEST
