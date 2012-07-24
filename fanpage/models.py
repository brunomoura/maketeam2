from django.db import models
ATIVO = 1
INATIVO = 0

class Fanpage(models.Model):
	STATUS_ESCOLHA = ((ATIVO, "ATIVO"), (INATIVO, "INATIVO"))

	nome = models.CharField(u"Nome", max_length=100)
	link_tab = models.CharField(u"Link da Tab",max_length=255)
	status = models.IntegerField(choices=STATUS_ESCOLHA, default=INATIVO)
