from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

TIPOOPE_CHOICES = (
	('Compra', 'Compra'),
	('Renta', 'Renta'),
	('Traspaso', 'Traspaso'),
	('Venta', 'Venta'),
)

TIPOINMUEBLE_CHOICES = (
	('Apartamento', 'Apartamento'),
	('Casa', 'Casa'),
	('Departamento', 'Departamento'),
	('Local', 'Local'),
	('Terreno', 'Terreno'),
)

TIPOMODNEDA_CHOICES = (
	('US Dollar', 'US Dollar'),
	('Pesos MX', 'Pesos MX'),
)


#class Moneda(models.Model):
	#nombre = models.CharField(max_length=25)

	#def __unicode__(self):
		#return self.nombre

#class Tipoinmueble(models.Model):
	#tipo = models.CharField(max_length=25)

	#def __unicode__(self):
		#return self.tipo


#class Tipooperacion(models.Model):
	#tipo = models.CharField(max_length=25)

	#def __unicode__(self):
		#return self.tipo
	

class Inmueble(models.Model):
	#usralta			= models.CharField('Usuario Alta', max_length=30)
	encabezado		= models.TextField('encabezado',max_length=500)
	tipoinmueble 	= models.CharField(max_length=25, choices=TIPOINMUEBLE_CHOICES, verbose_name='Tipo Inmueble')
	tipooperacion	= models.CharField(max_length=25, choices=TIPOOPE_CHOICES, verbose_name='Tipo Operacion')
	direccion		= models.CharField(max_length=200)
	precio			= models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
	moneda			= models.CharField(max_length=25, choices=TIPOMODNEDA_CHOICES, verbose_name='Moneda')
	banos			= models.IntegerField(default=0)
	vigilancia		= models.BooleanField(default=False)
	cocina			= models.BooleanField(default=False)
	sala			= models.BooleanField(default=False)
	cochera			= models.BooleanField(default=False)
	jardin			= models.BooleanField(default=False)
	mascotas		= models.BooleanField(default=False)
	canchatenis		= models.BooleanField(default=False)
	cargadescarga 	= models.BooleanField(default=False)
	alberca			= models.BooleanField(default=False)
	cuartolavado	= models.BooleanField(default=False)
	ac 				= models.BooleanField(default=False)
	cuartotv		= models.BooleanField(default=False)
	amueblado		= models.BooleanField(default=False)
	recamaras		= models.IntegerField(default=0)
	terreno			= models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
	tconstruccion	= models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
	excedente		= models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
	comentarios		= models.TextField(max_length=500)
	fecharegistro	= models.DateTimeField(auto_now_add=True)
	publicar		= models.BooleanField(default=True)

	def __unicode__(self):
		retorno = "%s - %s Direccion: %s"%(self.id, self.encabezado, self.direccion)
		return retorno

class Catalogoimg(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Inmueble/%s/%s"%(self.inmueble.id,filename)
		return ruta

	inmueble 		= models.ForeignKey(Inmueble)
	imagen			= models.ImageField(upload_to=url)
	imgportada		= models.BooleanField(default=False, verbose_name='Usar Como Imagen de portada')

	#def __unicode__(self):
		#return self.inmueble.id
