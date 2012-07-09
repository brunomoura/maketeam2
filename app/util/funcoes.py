from PIL import Image
import urllib2
import cStringIO
from django.conf import settings


def montar_imagem(dic):

	fundo = Image.open('/home/bruno/projetos django/maketeam2/maketeam/static/img/campo.jpg') 
	# dic = {"data" : [
	# {"id" : "100003016125914"	,"x": "40","y": "50"}]
	# }

	for i in range(0,11):
		x = "dados[%d][x]" % (i)
		y = "dados[%d][y]" % (i) 

		x = int(dic[x][0:3])-160 
		y = int(dic[y][0:3])-150
		
		user_id = "dados[%s][id]" % (str(i))
		url = "https://graph.facebook.com/%s/picture" % str(dic[user_id])

		foto = cStringIO.StringIO(urllib2.urlopen(url).read()) 
		foto = Image.open(foto)
		fundo.paste(foto, (x, y))

	fundo.save("/home/bruno/projetos django/maketeam2/maketeam/static/img/teste.jpg","jpeg")
	imagem = "/home/bruno/projetos django/maketeam2/maketeam/static/img/teste.jpg"
	return imagem
	
# def montar_marcacao(dic):

# 	tags = []

# 	for i in range(0,11):
# 		x = "dados[%d][x]" % (i)
# 		y = "dados[%d][y]" % (i) 

# 		x = int(dic[x][0:3])-160 
# 		y = int(dic[y][0:3])-150
		
# 		user_id = "dados[%s][id]" % (str(i))

# 		tags.append({'tag_uid': user_id, 'x': '30', 'y': '50'})

# 	return "'%s'" % tags