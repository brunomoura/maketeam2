from django.db import models

# Create your models here.
class Time(models.Model):
	tecnico = models.CharField(u'Tecnico', max_length=100)
	jogador1 = models.CharField(u'Jogador', max_length=100)
	jogador2 = models.CharField(u'Jogador', max_length=100)
	jogador3 = models.CharField(u'Jogador', max_length=100)
	jogador4 = models.CharField(u'Jogador', max_length=100)
	jogador5 = models.CharField(u'Jogador', max_length=100)	
	jogador6 = models.CharField(u'Jogador', max_length=100)
	jogador7 = models.CharField(u'Jogador', max_length=100)
	jogador8 = models.CharField(u'Jogador', max_length=100)
	jogador9 = models.CharField(u'Jogador', max_length=100)
	jogador10 = models.CharField(u'Jogador', max_length=100)
	jogador11 = models.CharField(u'Jogador', max_length=100)
	data = models.DateTimeField(auto_now=True)