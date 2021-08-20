from django.contrib import admin
from .models import Propiedad, Galeria

# Register your models here.


class GaleriaAdmin(admin.StackedInline):
    model = Galeria

class PropiedadAdmin(admin.ModelAdmin):
    list_display=["nombre","descripcion","operacion"]
    list_editable=["operacion"]
    search_fields=["nombre","descripcion"]
    inlines = [GaleriaAdmin]

    class Meta:
       model = Propiedad

class GaleriaAdmin(admin.ModelAdmin):
    list_display=["propiedad"]
    pass

admin.site.register(Propiedad, PropiedadAdmin)
