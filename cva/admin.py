from django.contrib import admin
from .models import Producto

from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin




class ProductoAdmin(ImportExportActionModelAdmin, ImportExportMixin, admin.ModelAdmin):
	list_display = ('descripcion','marca','clase','disponible','precio','moneda','disponibleCD','clave','codigo_fabricante','grupo')
	list_filter = ('marca','clase','moneda')
	search_fields = ('descripcion','codigo_fabricante','clave','marca','garantia','ficha_tecnica','ficha_comercial')


admin.site.register(Producto,ProductoAdmin)


