import requests
# import xml.etree.ElementTree as ET
import xmltodict
import json



def pedido(url):
	r=requests.get(url)
		

	try:
		data = xmltodict.parse(r.text)
		# return data['articulos']['item']
		pura_lista = data['articulos']['item']

		jsond=json.dumps(data['articulos']['item'])
		# print(data['articulos']['item'][0]['descripcion'])
		return pura_lista
	except:
		print('Nanai')

	return jsond

