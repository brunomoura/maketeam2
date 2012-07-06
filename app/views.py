# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from util.funcoes import montar_imagem
from facepy import GraphAPI
from facepy import SignedRequest

# @facebook_authorization_required
def time(request):
	friends = request.facebook.user.graph.get('me/friends')
	token = request.REQUEST["signed_request"]
	context = {}
	context['friends'] = json.dumps(friends['data'])
	context['token'] = token
	return render(request, 'time.html', context)

@csrf_exempt
def compartilhar(request):

	dados = request.POST
	token = request.POST['token']
	# user = dados["dados[8][id]"]
	imagem = montar_imagem(dados)
	
	signed_request = SignedRequest.parse(token, settings.FACEBOOK_APPLICATION_SECRET_KEY)
	graph = GraphAPI(signed_request['oauth_token'])
	post = graph.post(path="me/photos", tags="[{'tag_uid':'100003016125914', 'x':'30', 'y':'30'},{'tag_uid':'100003798651396'}]", message="Vote na sua banda favorita e acompanhem em tempo real essa disputa!!! acesse: http://apps.facebook.com/maketeam2", source=open(imagem))
	return HttpResponse(json.dumps(post))