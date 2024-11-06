Diagrama de modelo entidad-relación para el sistema de gestión de refugio de animales
Animales (Animals)

Atributos: animal_id (clave primaria, único), nombre, especie, raza, edad, sexo, tamaño, comportamiento, estado_médico_actual, etc.
Registros Médicos (Medical_Records)

Atributos: registro_id (clave primaria), fecha, detalles_médicos, tratamientos, próximos_exámenes
Relaciones: Un animal puede tener múltiples registros médicos.
Registros de Ingreso/Egreso (Intake_Outtake_Logs)

Atributos: log_id (clave primaria), fecha_ingreso, motivo_ingreso, fecha_egreso, motivo_egreso, destino
Relaciones: Cada log se asocia a un animal, y puede estar vinculado a un adoptante y un staff_voluntario.
Adoptantes (Adopters)

Atributos: adoptante_id (clave primaria), nombre, telefono, hijos, alergias, personas_hogar, tipo_casa, otros_animales, tipo_animal_acoger, num_animales_acoger, tamaño_sugerido, vivienda_asegurada, experiencia_animales, PPP
Relación Tipo Adopción: Un adoptante tiene un tipo de adopción (original, candidato, temporal, temporal con opción a definitiva, definitiva).
Opciones de Acogida Temporal: duración_acogida en semanas/meses para temporal, indefinido, posible_adopción, adopción_segura.
Adopciones (Adoptions)

Atributos: adopción_id (clave primaria), fecha_adopción, estado_adopción (pendiente, definitiva, cancelada)
Relaciones: Cada adopción está vinculada a un animal y a un adoptante.
Staff y Voluntarios (Staff_Volunteers)

Atributos: staff_voluntario_id (clave primaria), nombre, rol, telefono, email, fecha_inicio, horario_trabajo
Asociación (Association entre Intake/Outtake Logs)

Intake_Outtake_Logs se asocia con: animal_id, adoptante_id, y staff_voluntario_id


ADOPTER_EVALUATION - Interesado: Esta nueva entidad registra la evaluación del adoptante realizada por el staff o voluntario.
Campos:
evaluacion_id: Identificador único de la evaluación.
adoptante_id (FK): Identifica al adoptante evaluado.
staff_voluntario_id (FK): Identifica al staff o voluntario que realizó la evaluación.
fecha_evaluacion: Fecha en la que se realiza la evaluación.
concepto: Descripción de la evaluación.
color: Código de color basado en la clasificación:
Verde: Óptimos.
Verde Claro: Aptos.
Azul: Ya han acogido.
Amarillo: Aptos para perros enfermos.
Púrpura: Están presentes y pueden llevar al animal.
Rojo: No aptos.
Morado: Pueden acoger a PPP.
