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
from fanpage.models import Fanpage

@facebook_authorization_required
def time(request,fanpage_id=1):
	try:
		fanpage = Fanpage.objects.get(pk=fanpage_id)
		if not fanpage.status:
			fanpage_id = 1	
	except:
		fanpage_id = 1
	request.session['fanpage_id'] = fanpage_id
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
	nome_time = request.POST['nome_time']

	imagem = montar_imagem(dados, nome_time)

	if imagem == False:
		return HttpResponse("Nome de time invalido")

	tags = montar_marcacao(dados)
	
	tags = json.dumps(tags)
	
	signed_request = SignedRequest.parse(token, settings.FACEBOOK_APPLICATION_SECRET_KEY)
	graph = GraphAPI(signed_request['oauth_token'])
	post = graph.post(path="me/photos", tags=tags, message="Monte seu time de futebol com seus amigos!!! acesse: http://apps.facebook.com/maketeam", source=open(imagem))
	return HttpResponse(json.dumps(post))