from django.http import HttpResponse
from drbreaker.models import Team
# Create your views here.
def scores(request):
	team_list = Team.objects.all().order_by('-score')
	output = "<h1>Scorebord</h1><ul>" 
	for t in team_list:
		output += "<li>" + t.name + ":" + str(t.score) + " </li>"
	output += "</ul>"
	return HttpResponse(output)
