import Image
import urllib2
import cStringIO
import os

def montar_imagem():

	foto = cStringIO.StringIO(urllib2.urlopen("http://profile.ak.fbcdn.net/hprofile-ak-snc4/50084_100003016125914_1874164856_q.jpg").read())
	


	foto = Image.open(foto)

	fundo = Image.open("campo.jpg") 

	fundo.paste(foto, (70,193))

	fundo.save("teste.jpg","jpeg")
	
	# asdasd = {"data" : [
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"},
	# {"id" : "121231"	,"x": "4","y": "5"}]
	# }

montar_imagem()