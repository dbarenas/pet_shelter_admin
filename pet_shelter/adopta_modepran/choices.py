from django.db import models


class Choices(models.Model):
    tipo = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    )

    sexo = (
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
     )

    situacao = (
        ('Ativado', 'Ativado'),
        ('Desativado', 'Desativado'),
    )

    experiencia = (
        ('Si', 'Si'),
        ('No', 'No'),
     )

    num_animales_acoger = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    TAMANO = (
        ('S', 'Pequeño -8KG'),
        ('M', 'Mediano 8KG-20KG'),
        ('L', 'Grande 20KG-35KG'),
        ('XL', 'Mas Grande +35KG'),
    )

    TIEMPO_ACOGIDA = (
        ('1', 'SEMANAS'),
        ('2', 'MESES'),
        ('3', 'TEMPORAL'),
        ('4', 'INDEFINIDO'),
        ('5', 'OPCIÓN ADOPCIÓN'),
    )