# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from fandjango.decorators import facebook_authorization_required
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from util.funcoes import montar_imagem

# @facebook_authorization_required
def time(request):
	friends = request.facebook.user.graph.get('me/friends')
	context = {}
	context['friends'] = json.dumps(friends['data'])

	return render(request, 'time.html', context)

@csrf_exempt
def compartilhar(request):

	dados = request.POST

	# user = dados["dados[8][id]"]
	imagem = montar_imagem(dados)
	return HttpResponse(imagem)
	signed_request = SignedRequest.parse(token, settings.FACEBOOK_APPLICATION_SECRET_KEY)
	graph = GraphAPI(signed_request.oauth_token.token)
	post = graph.post(path="me/photos", tags="[{'tag_uid':'100003016125914'},{'tag_uid':'100003798651396'}]", message="Vote na sua banda favorita e acompanhem em tempo real essa disputa!!! acesse: http://apps.facebook.com/maketeam2", source=open(settings.STATIC_ROOT+"/media/"+imagem))
	return HttpResponse(simplejson.dumps(post))