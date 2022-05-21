from django.contrib import admin
from .models import Persona,Hablidades
# Register your models here.

admin.site.register(Hablidades)

class EmpleadosAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'lastName',
        'departamento',
        'job',
        'full_name',
    )
    #
    def full_name(self, obj):
        print(obj)
        return f'{obj.name} {obj.lastName}'
    def id(sefl, obj):
        return obj.id
    #

    # Buscador
    search_fields=('name',)
    # filtro de busqueda
    list_filter=('job','habilidades')
    # filtro para muchos a muchos
    # Escoger de mejor manera las habilidades
    filter_horizontal=('habilidades',)
admin.site.register(Persona, EmpleadosAdmin)
