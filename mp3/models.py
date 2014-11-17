from django.db import models
from musica.settings import MEDIA_ROOT
from django.contrib.auth.models import User



class perfil(models.Model):
	def get_ruta(self,filename):
		ruta_completa = "%s%s" %(MEDIA_ROOT,user.username)
		return ruta_completa

	user = models.OneToOneField(User,null=False,blank=False)
	foto = models.ImageField(upload_to=get_ruta)


class mp3(models.Model):
	def get_ruta(self,filename):
		ruta_completa = "%s%s" %(MEDIA_ROOT,user.username)
		return ruta_completa
	user = models.OneToOneField(User,null=False,blank=False)
	mp3 = models.FileField(upload_to=get_ruta)
