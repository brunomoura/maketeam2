# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from util.funcoes import montar_imagem, montar_marcacao
from facepy import GraphAPI
from facepy import SignedRequest

# @facebook_authorization_required
def time(request):
	friends = request.facebook.user.graph.get('me/friends')
	usuario = {u"name": request.facebook.user.first_name+' '+request.facebook.user.last_name, u"id": request.facebook.user.facebook_id} 
	friends['data'].append(usuario)
	token = request.REQUEST["signed_request"]
	context = {}
	context['friends'] = json.dumps(friends['data'])
	
	context['token'] = token
	return render(request, 'time.html', context)

@csrf_exempt
def compartilhar(request):

	dados = request.POST
	token = request.POST['token']
	imagem = montar_imagem(dados)

	tags = montar_marcacao(dados)
	
	tags = json.dumps(tags)
	
	signed_request = SignedRequest.parse(token, settings.FACEBOOK_APPLICATION_SECRET_KEY)
	graph = GraphAPI(signed_request['oauth_token'])
	post = graph.post(path="me/photos", tags=tags, message="Vote na sua banda favorita e acompanhem em tempo real essa disputa!!! acesse: http://apps.facebook.com/maketeam2", source=open(imagem))
	return HttpResponse(json.dumps(post))