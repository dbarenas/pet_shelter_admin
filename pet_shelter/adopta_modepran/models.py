from django.db import models


TIPO = (
    ('Perro', 'Perro'),
    ('Gato', 'Gato'),
)

SEXO = (
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),
)

STATUS = (
    ('Activo', 'Activo'),
    ('Desactivado', 'Desactivado'),
)

EXPERIENCIA = (
    ('Si', 'Si'),
    ('No', 'No'),
)
PROTECTORA = (
    ('0', 'Si'),
    ('1', 'No'),
)

ORIGEN = (
    ('Particular', 'Particular'),
    ('Protectora', 'Protectora'),
)
NUM_ANIMALES_ACOGER = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

TAMANO = (
    ('S', 'Pequeño -8KG'),
    ('M', 'Mediano 8KG-20KG'),
    ('L', 'Grande 20KG-35KG'),
    ('XL', 'Mas Grande +35KG'),
)

TIEMPO_ACOGIDA = (
    ('SEMANAS', 'SEMANAS'),
    ('MESES', 'MESES'),
    ('TEMPORAL', 'TEMPORAL'),
    ('INDEFINIDO', 'INDEFINIDO'),
    ('POSIBLE ADOPCIÓN', 'POSIBLE ADOPCIÓN'),
)

class ControlesMedico(models.Model):
    fecha = models.DateField()
    detalles_medicos = models.TextField(blank=True, null=True)
    tratamientos = models.TextField(blank=True, null=True)
    proximos_examenes = models.DateField(blank=True, null=True)
    centro_veterinario = models.CharField(max_length=100)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, related_name='medical_records')

class Animal(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO)
    sexo = models.CharField(max_length=10, choices=SEXO)
    caracteristicas = models.TextField(blank=True, null=True)
    origen = models.CharField(max_length=50, choices=ORIGEN)
    protectora = models.ForeignKey('Adopter', on_delete=models.CASCADE, null=True, blank=True, related_name='adopter')
    rivia_reiac = models.CharField(max_length=50)
    registrado = models.DateTimeField()
    incidencia = models.TextField(blank=True, null=True)
    observaciones_adiestramiento = models.TextField(blank=True, null=True)
    recomendaciones_adiestrador = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    estado_medico_actual = models.TextField(blank=True, null=True)
    social_media_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.numero} - {self.tipo} - ({self.sexo})"


class Adopter(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    esprotectora =  models.BooleanField(default=False)
    telefono = models.CharField(max_length=20)
    hijos = models.IntegerField(blank=True, null=True)
    alergias =  models.BooleanField(default=False)
    personas_hogar = models.IntegerField(blank=True, null=True)
    tipo_casa = models.CharField(max_length=50, blank=True, null=True)
    otros_animales = models.TextField(blank=True, null=True)
    tipo_animal_acoger = models.CharField(max_length=30, blank=True, null=True, choices=TIPO)
    tamano_preferido = models.CharField(max_length=15, blank=True, null=True, choices=TAMANO)
    tiempo_acogida = models.CharField(max_length=20, choices=TIEMPO_ACOGIDA)
    PPP =  models.BooleanField(default=False)
    correo_electronico = models.CharField(max_length=100, blank=True, null=True)
    vivienda_protegida = models.BooleanField(default=False)
    experiencia_animales = models.BooleanField(default=False)
    num_animales_acoger = models.IntegerField(blank=True, null=True, choices=NUM_ANIMALES_ACOGER)
    observacion_1 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - Es protectora:{self.esprotectora}  |  experiencia_animales :({self.experiencia_animales})"

class StaffVoluntario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    rol = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_inicio = models.DateField(blank=True, null=True)
    horario_trabajo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - ({self.rol})"

class RegistroAcceso(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adopter, on_delete=models.CASCADE, null=True, blank=True)
    staff_voluntario = models.ForeignKey(StaffVoluntario, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.DateField()
    motivo_ingreso = models.TextField(blank=True, null=True)
    fecha_egreso = models.DateField(blank=True, null=True)
    motivo_egreso = models.TextField(blank=True, null=True)
    destino = models.TextField(blank=True, null=True)

COLOR_EVALUACION = (
    ('#008000', 'Verde: Óptimos'),  # Green
    ('#90EE90', 'Verde Claro: Aptos'),  # Light Green
    ('#0000FF', 'Azul: Ya han acogido'),  # Blue
    ('#FFFF00', 'Amarillo: Aptos para perros enfermos'),  # Yellow
    ('#800080', 'Púrpura: Están presentes y pueden llevar al animal'),  # Purple
    ('#FF0000', 'Rojo: No aptos'),  # Red
    ('#8A2BE2', 'Morado: Pueden acoger a PPP'),  # BlueViolet
)

class Interesado(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    staff_voluntario = models.ForeignKey(StaffVoluntario, on_delete=models.CASCADE, null=True, blank=True)
    fecha_interes = models.DateField()
    estado_interes = models.CharField(max_length=30, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    color_evaluacion = models.CharField(max_length=50, blank=True, null=True, choices=COLOR_EVALUACION)

