from django.db import models



class Producto(models.Model):
	clave = models.CharField(max_length=200,blank=True,null=True)
	codigo_fabricante = models.CharField(max_length=200,blank=True,null=True)
	descripcion = models.TextField(blank=True,null=True)
	grupo = models.CharField(max_length=200,blank=True,null=True)
	marca = models.CharField(max_length=200,blank=True,null=True)
	garantia = models.CharField(max_length=200,blank=True,null=True)
	clase = models.CharField(max_length=200,blank=True,null=True)
	disponible = models.CharField(max_length=200,blank=True,null=True)
	precio = models.CharField(max_length=200,blank=True,null=True)
	moneda = models.CharField(max_length=200,blank=True,null=True)
	ficha_tecnica = models.CharField(max_length=200,blank=True,null=True)
	ficha_comercial = models.CharField(max_length=200,blank=True,null=True)
	imagen = models.URLField(null=True,blank=True)
	disponibleCD = models.CharField(max_length=200,blank=True,null=True)
	total_descuento = models.CharField(max_length=200,blank=True,null=True)
	moneda_descuento = models.CharField(max_length=200,blank=True,null=True)
	precio_descuento = models.CharField(max_length=200,blank=True,null=True)
	moneda_precio_descuento = models.CharField(max_length=200,blank=True,null=True)
	clave_promocion = models.CharField(max_length=200,blank=True,null=True)
	descripcion_promocion = models.CharField(max_length=200,blank=True,null=True)
	vencimiento_promocion = models.CharField(max_length=200,blank=True,null=True)
	disponible_en_promocion = models.CharField(max_length=200,blank=True,null=True)
	en_promo = models.NullBooleanField(blank=True,null=True,default=False)

	def __str__(self):
		return self.clave
