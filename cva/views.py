from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.core import serializers
from .models import Producto

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

class Indexar(View):
	def get(self,request):
		template="cva/home.html"
		url = 'https://www.grupocva.com/catalogo_clientes_xml/lista_precios.xml?cliente=24808&marca=%25&grupo=%25&clave=%25&codigo=%25'
		data = utils.pedido(url)
		for item in data:
			try:
				p = Producto.objects.get(clave=item['clave'],descripcion=item['descripcion'])
				print('Producto ya existe',p)

			except:

				p = Producto()

				p.clave = item['clave']
				p.codigo_fabricante = item['codigo_fabricante']
				p.descripcion = item['descripcion']
				p.marca = item['marca']
				p.garantia = item['garantia']
				p.clase = item['clase']
				p.disponible = item['disponible']
				p.precio = item['precio']
				p.moneda = item['moneda']
				p.ficha_tecnica = item['ficha_tecnica']
				p.ficha_comercial = item['ficha_comercial']
				p.imagen = item['imagen']
				p.disponibleCD = item['disponibleCD']

				p.save()

		return render(request,template)

	def post(self,request):
		Producto.objects.all().delete()
		return redirect('cva:index')
