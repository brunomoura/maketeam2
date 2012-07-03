# Create your views here.
from django.shortcuts import render
from fandjango.decorators import facebook_authorization_required
import json

# @facebook_authorization_required
def time(request):
	friends = request.facebook.user.graph.get('me/friends')
	context = {}
	context['friends'] = json.dumps(friends['data'])

	return render(request, 'time.html', context)