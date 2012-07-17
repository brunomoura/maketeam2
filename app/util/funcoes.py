from PIL import Image, ImageDraw, ImageFont
import urllib2
import cStringIO
from django.conf import settings


def montar_imagem(dic, nome_time):

	fundo = Image.open(settings.STATICFILES_DIRS[0]+'/img/campo.jpg')
	fontFile = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
	font = ImageFont.truetype(fontFile, 20)

	draw = ImageDraw.Draw(fundo)
	draw.text((2,2), nome_time, font=font)
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
	
	
	try:
		imagem = settings.MEDIA_ROOT+"/user_upload/%s.jpg" % nome_time
		fundo.save(imagem) 
	except:
		imagem = False
	return imagem
	
def montar_marcacao(dic):

	tags = []

	for i in range(0,11):
		x = "dados[%d][x]" % (i)
		y = "dados[%d][y]" % (i)  

		x = ((int(dic[x][0:3])-150)*100)/391
		y = ((int(dic[y][0:3])-160)*100)/626
		
		x = str(x)
		y = str(y)
		
		user_id = "dados[%s][id]" % (str(i))
		user_id = str(dic[user_id])
		tags.append({'tag_uid': user_id, 'x': x, 'y': y})

	return tags