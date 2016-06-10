from django.contrib import admin
from .models import Producto

from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin




class ProductoAdmin(ImportExportActionModelAdmin, ImportExportMixin, admin.ModelAdmin):
	list_display = ('en_promo','descripcion','precio','precio_descuento','total_descuento','disponible_en_promocion','moneda','moneda_descuento','moneda_precio_descuento','clave_promocion','descripcion_promocion','vencimiento_promocion','disponible','disponibleCD','marca','clase','clave','codigo_fabricante','grupo',)
	list_filter = ('en_promo','moneda','disponible_en_promocion','total_descuento')
	search_fields = ('descripcion','codigo_fabricante','clave','marca','garantia','ficha_tecnica','ficha_comercial','descripcion_promocion')


admin.site.register(Producto,ProductoAdmin)


