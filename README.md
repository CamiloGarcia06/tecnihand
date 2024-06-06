Módulo de Gestión de Repositorios para Odoo 17
Resumen

Este módulo proporciona funcionalidades para gestionar repositorios Git y commits dentro de Odoo 17. Incluye:

    Crear y gestionar repositorios Git.
    Rastrear y visualizar commits.
    Restringir el acceso a registros de repositorios y commits según roles de usuario.

Se introducen dos roles de usuario:

    Gestor de Repositorios: Puede crear, leer, actualizar y eliminar repositorios y commits.

Funcionalidades
Grupos de Usuarios

    Gestor de Repositorios:
        Acceso completo CRUD (Crear, Leer, Actualizar, Eliminar) a repositorios y commits.
        Capacidad para realizar acciones especiales en los repositorios.

Vistas y Botones

    Vistas de formulario y lista para repositorios y commits, configuradas para mostrar información relevante.
    Botón de Acción Especial: Visible solo para usuarios en el grupo "Gestor de Repositorios", permitiendo la ejecución de acciones específicas en los repositorios.

Endpoints

Se proporciona un endpoint basado en JSON para obtener detalles de repositorios y commits para un socio específico:

    Endpoint: /api/repositories/<partner_id>
    Método: POST
    Autenticación: Pública
    Respuesta: JSON con detalles del socio, información del repositorio y los últimos 10 commits.

Instalación
Prerrequisitos

    Odoo 17
    Acceso administrativo al servidor de Odoo
    Conocimientos básicos sobre instalación y configuración de módulos en Odoo

Pasos

    Clonar el Módulo: Coloca el directorio del módulo en el directorio de addons de Odoo.

    bash

cd /path/to/odoo/addons
git clone https://github.com/CamiloGarcia06/tecnihand.git

Actualizar Odoo: Reinicia Odoo y actualiza la lista de módulos.

bash

    sudo systemctl restart odoo

    Instalar el Módulo: Ve al menú de Apps en Odoo, busca "Gestión de Repositorios" e instálalo.

    Configurar Acceso de Usuarios: Asigna a los usuarios los grupos adecuados (Gestor de Repositorios o Visualizador de Repositorios) a través de la configuración de usuarios en Odoo.

Uso
Gestión de Repositorios y Commits

    Navegar a Repositorios: Ve al menú "Repositorios" en la sección de Gestión de Proyectos.
    Crear un Repositorio: Haz clic en "Crear" y completa los detalles del repositorio.
    Ver Commits: Accede al menú "Commits" dentro de un repositorio para ver los últimos commits.

Endpoint API

    URL: http://<tu-servidor-odoo>/api/repositories/<partner_id>
    Método: POST
    Encabezados: Content-Type: application/json
    Carga Útil: Objeto JSON vacío {}

Ejemplo de Solicitud Usando curl

bash

curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:8069/api/repositories/1

Ejemplo de Solicitud Usando Python

python

import requests

url = 'http://localhost:8069/api/repositories/1'
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, json={})
print(response.json())

Configuración
Adición Manual de Registros

Los repositorios y commits se pueden agregar manualmente a través de la interfaz de Odoo:

    Repositorios: En el menú "Repositorios", utiliza el botón "Crear".
    Commits: Dentro de la vista de formulario de un repositorio, añade commits directamente.

Visibilidad del Botón

El Botón de Acción Especial en la vista de formulario del repositorio está restringido a usuarios en el grupo Gestor de Repositorios. Esto se controla a través del atributo groups en la definición de la vista XML.
Detalles Técnicos
Seguridad

    Grupos: Definidos en repository_security.xml con derechos de acceso específicos.
    Reglas: Las reglas de acceso diferencian entre gestores y visualizadores.

Vistas

    Vistas de Formulario y Lista: Definidas en repository_views.xml, git_commit_views.xml, git_menus_views y res_partner_views para proporcionar una interfaz amigable para la gestión de repositorios y commits.

Controlador API

    Controlador: Definido en main.py para manejar solicitudes JSON de datos de repositorios basados en el ID del socio.

Mejoras Futuras

    Automatización: Integrar la obtención automática de commits desde repositorios Git reales.
    Mejoras en la UI: Mejorar la interfaz de usuario para una mejor experiencia.
    Características Adicionales: Añadir análisis más detallados e informes de actividades de repositorios.

Soporte

Para problemas o solicitudes de características, utiliza la página de Issues de GitHub.
Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

Este README.md proporciona una descripción clara del módulo, instrucciones de instalación, detalles de uso y una breve descripción técnica en español. Ajusta las URLs y rutas según tu configuración específica y tu repositorio de GitHub.
