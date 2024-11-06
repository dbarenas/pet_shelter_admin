# Proyecto Pet Shelter

## Descripción
Pet Shelter es un sistema desarrollado en Django para gestionar la adopción de animales, el seguimiento de acceso e interés de adoptantes, así como la gestión del personal voluntario y controles médicos de los animales en protectoras. El proyecto tiene como objetivo facilitar la gestión de animales en protectoras y el proceso de adopción, mejorando la experiencia de adopción tanto para los animales como para los adoptantes.

## Características
- Gestión de animales (información general, estado de salud, historial de adopciones).
- Evaluación de adoptantes por parte del staff o voluntarios, con clasificación mediante códigos de colores.
- Seguimiento del interés de adoptantes y su progreso.
- Gestión del personal voluntario y sus registros de acceso.

## Tecnologías Utilizadas
- **Backend**: Django, SQLite
- **Frontend**: HTML, CSS (con Bootstrap)
- **Entorno de Desarrollo**: Python 3, entorno virtual con `venv`

## Requisitos Previos
- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación
1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/pet_shelter.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd pet_shelter
   ```
3. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate
   ```
4. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```
5. Realiza las migraciones iniciales:
   ```bash
   python manage.py migrate
   ```
6. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
7. Accede a la aplicación desde tu navegador en `http://127.0.0.1:8000/`.

## Uso
- Puedes gestionar animales, adoptantes, voluntarios y su información correspondiente desde la interfaz web del proyecto.
- El panel de administración de Django está disponible para usuarios autorizados en `http://127.0.0.1:8000/admin/`.

## Estructura del Proyecto
- **pet_shelter/**: Carpeta principal del proyecto que contiene configuraciones generales.
- **adopta_modepran/**: Aplicación principal que gestiona la lógica de adopción.
- **templates/**: Archivos HTML utilizados para las vistas.
- **models.py**: Definición de las entidades y sus relaciones en la base de datos.
- **views.py**: Lógica para procesar las solicitudes HTTP y retornar las respuestas.
- **urls.py**: Configuración de las rutas de la aplicación.

## Contribuir
Las contribuciones son bienvenidas. Si deseas colaborar, sigue los siguientes pasos:
1. Realiza un fork del proyecto.
2. Crea una rama para tu característica o corrección (`git checkout -b nombre-rama`).
3. Realiza tus cambios y haz commit (`git commit -m 'Descripción del cambio'`).
4. Envía un pull request a la rama principal del proyecto.

## Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## Contacto
- **Autor**: Nombre del Autor
- **Email**: correo@ejemplo.com
- **GitHub**: [https://github.com/usuario](https://github.com/usuario)

---
Sí tienes alguna pregunta o sugerencia, no dudes en contactarme.

