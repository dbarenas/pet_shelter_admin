from django.contrib import admin
from django import forms
from .models import COLOR_EVALUACION,ControlesMedico, Animal, Adopter, StaffVoluntario, RegistroAcceso, Interesado


class MyAdminSite(admin.AdminSite):
    site_header = "Gestion Adopciones Modepran"  # Change the header text
    site_title = "Gestion Adopciones Modepran"  # Change the title text shown in the browser tab
    index_title = "Hola Bienvenider - Gestion Adopciones Modeprann"  # Change the title on the main admin page

# Register your custom admin site
admin_site = MyAdminSite(name='myadmin')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'numero', 'sexo', 'origen', 'created', 'edited')
    list_filter = ('tipo', 'sexo', 'origen')  # Fields to filter by
    search_fields = ('tipo', 'numero', 'origen')  # Search by these fields


@admin.register(ControlesMedico)
class ControlesMedicoAdmin(admin.ModelAdmin):
    list_display = ('animal', 'proximos_examenes', 'centro_veterinario')
    list_filter = ('animal', 'proximos_examenes', 'centro_veterinario') # Fields to filter by
    search_fields = ('animal', 'proximos_examenes', 'centro_veterinario')  # Search by these fields

@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'telefono', 'hijos', 'alergias', 'tipo_animal_acoger', 'tamano_preferido', 'experiencia_animales')
    list_filter = ('esprotectora', 'alergias', 'tipo_animal_acoger', 'tamano_preferido', 'tiempo_acogida')
    search_fields = ('nombre', 'apellidos', 'telefono', 'correo_electronico', 'otros_animales')

admin.site.register(StaffVoluntario)
@admin.register(RegistroAcceso)
class RegistroAccesoAdmin(admin.ModelAdmin):
    list_display = (
        'animal',
        'adoptante',
        'staff_voluntario',
        'fecha_ingreso',
        'motivo_ingreso',
        'fecha_egreso',
        'motivo_egreso',
        'destino'
    )
    list_filter = ('animal', 'adoptante', 'staff_voluntario', 'fecha_ingreso', 'fecha_egreso')
    search_fields = ('animal__nombre', 'adoptante__nombre', 'staff_voluntario__nombre', 'motivo_ingreso', 'motivo_egreso', 'destino')

@admin.register(Interesado)
class InteresadoAdmin(admin.ModelAdmin):
    form = forms.ModelForm
    list_display = ('animal', 'adoptante', 'staff_voluntario', 'color_evaluacion')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "color_evaluacion":
            # Create a custom widget that shows both color and text
            choices = [(color, f'<span style="color:{color};">{text}</span>') for color, text in COLOR_EVALUACION]
            kwargs['widget'] = forms.Select(choices=choices)
            kwargs['widget'].attrs['style'] = 'width: auto;'  # Adjust width if necessary
        return super().formfield_for_dbfield(db_field, request, **kwargs)


