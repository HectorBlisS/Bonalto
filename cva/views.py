from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.core import serializers
from .models import Producto

from django.contrib import messages

from . import utils





class Home(View):
	def get(self,request):
		template="cva/home.html"
		# url = 'https://www.grupocva.com/catalogo_clientes_xml/lista_precios.xml?cliente=24808&marca=%25&grupo=%25&clave=%25&codigo=%25'
		# data = utils.pedido(url)

		# context={
		# 'data':data
		# }
		
		# return HttpResponse(data,content_type='application/json')
		return render(request,template)

	def post(self,request):
		template="cva/home.html"
		try:
			Producto.objects.all().delete()
			messages.success(request,'Base de datos Borrada')
		except:
			messages.error(request,'No se pudo borrar')
		return render(request,template)


class Indexar(View):
	def get(self,request):
		# template="cva/home.html"
		contador = 0
		prods = 0
		url = 'https://www.grupocva.com/catalogo_clientes_xml/lista_precios.xml?cliente=24808&marca=%25&grupo=%25&clave=%25&codigo=%25'
		try:
			data = utils.pedido(url)
			# for item in data:
			# 	try:
			# 		p = Producto.objects.get(clave=item['clave'],descripcion=item['descripcion'])
			# 		messages.info(request,'Producto ya existe {}'.format(p))
			# 		contador+=1

			# 	except:
					
			# 		p = Producto()

			# 		p.clave = item['clave']
			# 		p.codigo_fabricante = item['codigo_fabricante']
			# 		p.descripcion = item['descripcion']
			# 		p.marca = item['marca']
			# 		p.garantia = item['garantia']
			# 		p.clase = item['clase']
			# 		p.disponible = item['disponible']
			# 		p.precio = item['precio']
			# 		p.moneda = item['moneda']
			# 		p.ficha_tecnica = item['ficha_tecnica']
			# 		p.ficha_comercial = item['ficha_comercial']
			# 		p.imagen = item['imagen']
			# 		p.disponibleCD = item['disponibleCD']

			# 		p.save()
					# messages.success(request,'Producto agregado!')
					# prods+=1
			messages.success(request,'Producto agregado!')
			prods+=1
		except Exception as e:
			messages.error(request,'Esta mierda falla {}'.format(e))

		messages.warning(request,'Productos agregados: {} \n Productos repetidos: {}'.format(prods,contador))
		return redirect('cva:home')



