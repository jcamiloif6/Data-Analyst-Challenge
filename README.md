# Migración de Datos CSV a MySQL y Creación de Dashboard en Power BI

Este repositorio contiene un flujo de trabajo completo para la migración de archivos CSV a una base de datos MySQL utilizando MySQL Workbench. El proyecto incluye la inserción automatizada de datos desde archivos CSV a MySQL, la construcción de consultas SQL y la visualización de los datos mediante un dashboard en Power BI conectado directamente a MySQL Workbench.
## Contenido del Repositorio:

  ### Migración de CSV a MySQL:
  - Script en Python con una API REST para cargar archivos CSV y migrar los datos a tablas en MySQL.
  - Gestión automática de la creación de tablas en base a la estructura del archivo CSV.
  ### Consultas SQL:
  - Conjunto de consultas SQL para explorar y analizar los datos migrados.
  ### Dashboard en Power BI:
  - Conexión directa a MySQL Workbench desde Power BI para visualización de datos.
  - Reportes dinámicos y visualizaciones personalizadas utilizando Power BI para obtener insights de los datos.

## Tecnologías Utilizadas:

- Python: Para la creación de la API REST que gestiona la migración de archivos CSV a MySQL.
- MySQL Workbench: Para almacenar y consultar los datos.
- Power BI: Para la creación del dashboard interactivo basado en los datos almacenados en MySQL.

## Prerrequisitos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

### Python 3: Para ejecutar los scripts y la API REST.
- Instala Python desde [python.org](https://www.python.org/downloads/)
- Requiere bibliotecas adicionales como Flask, mysql-connector-python, y datetime. Puedes instalarlas ejecutando:

        pip install flask mysql-connector-python

- MySQL Workbench: Para crear la base de datos y gestionar las consultas SQL.
        Descárgalo desde [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

- Power BI Desktop: Para crear y visualizar el dashboard.
        Descárgalo desde [Power BI Desktop](https://www.microsoft.com/en-us/power-platform/products/power-bi/desktop)

- Acceso a MySQL Server: Asegúrate de tener configurada tus credenciales a una instancia de MySQL Server local.

## Instrucciones de Uso

- Clonar el Repositorio:

        git clone https://github.com/usuario/repositorio.git

- Ejecutar la API REST(codigo para insertar datos):

### Opcion 1

        python3 app2.py
### Opcion 2

        python app2.py

- Usa curl en consola o herramientas como Postman para subir los archivos CSV y migrarlos a la base de datos MySQL.
  
        curl -X POST -F 'file=@/ruta/al/archivo.csv' http://127.0.0.1:5000/upload_csv

- Conectar Power BI a MySQL Workbench:
  
Configura la conexión a la base de datos MySQL desde Power BI para cargar y visualizar los datos migrados.

Sigue este tutorial: [youtube.com](https://www.youtube.com/watch?v=hWIVznIhc6o)
