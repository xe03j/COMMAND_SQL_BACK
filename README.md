# CommandSQL API

Bienvenido al repositorio del proyecto **CommandSQL API**, un backend educativo y gamificado para aprender comandos SQL mediante misiones, logros y un sistema de progreso.

Este backend está desarrollado con **FastAPI** y se conecta a una base de datos PostgreSQL para gestionar usuarios, autenticación, misiones, logros y el avance de los jugadores.

## API en Producción

- La API ya está desplegada en:

```bash
https://command-sql-back.onrender.com/
```

## Estructura del Proyecto

- **Autenticación**: Manejo de usuarios y sesiones con JWT.  
- **Misiones**: Endpoints para crear, consultar y validar misiones SQL.  
- **Logros**: Sistema de recompensas para motivar el aprendizaje.  
- **Progreso**: Seguimiento del avance de cada usuario.  
- **Manual**: Documentación básica para apoyo al jugador.  

La documentación interactiva de la API está disponible en:

- Swagger UI → `/docs`  
- Redoc → `/redoc`  

## Tecnologías Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) para el desarrollo del backend.  
- [SQLAlchemy](https://www.sqlalchemy.org/) para la conexión con la base de datos.  
- [PostgreSQL](https://www.postgresql.org/) como gestor de base de datos.  
- [Alembic](https://alembic.sqlalchemy.org/) para migraciones.  
- [PyJWT](https://pyjwt.readthedocs.io/) para la autenticación con tokens JWT.  
- [Uvicorn](https://www.uvicorn.org/) como servidor ASGI.  

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clona el repositorio
```bash
git clone https://github.com/xe03j/COMMAND_SQL_BACK.git
```

### 2. Crea y activa un entorno virtual si es tu caso
```bash
python -m venv venv
source venv/bin/activate   # Linux / MacOS
venv\Scripts\activate      # Windows
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno
Crea un archivo **.env** en la raíz del proyecto con el siguiente contenido:

```
DATABASE_URL=postgresql://usuario:password@localhost:5432/tu_db
```

### 5. Crea la BD en POSTGRSQL, la BD de crearse antes de ejcutar la API


### 6. Inicia el servidor de desarrollo
```bash
uvicorn main:app --reload
```

La API estará disponible en:
```bash
http://127.0.0.1:8000
```

## Ramas

- **master** → versión local para desarrollo.  
- **despliegue** → versión configurada para producción (Render).  

## Notas

- Si usas el proyecto junto con el **frontend**, asegúrate de que las URLs coincidan (local o producción).  
- En despliegue gratuito (Render), los primeros requests pueden tardar hasta 1 minuto. 


## Notas 2

- Para funcionar ocupas estos json con misiones, niveles y logros


- JSON NIVELES usa el ENDPOINT /niveles/bulk_create:
```bash
[
    {
      "id_nivel": 1,
      "titulo": "Reactivar el núcleo de datos",
      "descripcion": "La nave perdió toda su base de datos central tras la tormenta. Debes crear una nueva base de datos llamada 'nave_estrella'.",
      "dificultad": "Fácil",
      "tema_sql": "CREATE DATABASE"
    },
    {
      "id_nivel": 2,
      "titulo": "Reconstruir registros de tripulación",
      "descripcion": "El sistema de soporte vital necesita saber quién sigue a bordo. Crea una tabla llamada 'tripulacion' con columnas: id SERIAL PRIMARY KEY, nombre VARCHAR(50), rol VARCHAR(50).",
      "dificultad": "Fácil",
      "tema_sql": "CREATE TABLE"
    },
    {
      "id_nivel": 3,
      "titulo": "Cargar la tripulación al sistema",
      "descripcion": "Inserta los tripulantes iniciales en la tabla tripulacion: (Ana, Piloto), (José, Ingeniero), (Luisa, Médica).",
      "dificultad": "Fácil",
      "tema_sql": "INSERT"
    },
    {
      "id_nivel": 4,
      "titulo": "Verificar tripulación activa",
      "descripcion": "Necesitamos listar todos los tripulantes registrados. Usa un SELECT para mostrar id, nombre y rol.",
      "dificultad": "Fácil",
      "tema_sql": "SELECT"
    },
    {
      "id_nivel": 5,
      "titulo": "Purgar datos dañados",
      "descripcion": "Uno de los registros está corrupto. Elimina al tripulante con nombre 'José' de la tabla tripulacion.",
      "dificultad": "Medio",
      "tema_sql": "DELETE"
    },
    {
      "id_nivel": 6,
      "titulo": "Actualizar rol de emergencia",
      "descripcion": "Luisa ahora es la Comandante temporal de la nave. Actualiza su rol en la tabla tripulacion.",
      "dificultad": "Medio",
      "tema_sql": "UPDATE"
    },
    {
      "id_nivel": 7,
      "titulo": "Crear sistema de recursos",
      "descripcion": "El módulo de energía necesita controlarse. Crea una tabla 'recursos' con columnas: id SERIAL PRIMARY KEY, tipo VARCHAR(50), cantidad INT.",
      "dificultad": "Fácil",
      "tema_sql": "CREATE TABLE"
    },
    {
      "id_nivel": 8,
      "titulo": "Reabastecer la nave",
      "descripcion": "Inserta recursos iniciales en la tabla: (Oxígeno, 100), (Combustible, 500), (Agua, 200).",
      "dificultad": "Fácil",
      "tema_sql": "INSERT"
    },
    {
      "id_nivel": 9,
      "titulo": "Revisar estado de recursos",
      "descripcion": "Necesitamos saber qué recursos son menores a 300 unidades. Haz un SELECT filtrando con WHERE.",
      "dificultad": "Medio",
      "tema_sql": "SELECT WHERE"
    },
    {
      "id_nivel": 10,
      "titulo": "Asignar recursos por tripulante",
      "descripcion": "Crea una nueva tabla 'asignaciones' con columnas: id SERIAL PRIMARY KEY, tripulante_id INT REFERENCES tripulacion(id), recurso_id INT REFERENCES recursos(id). Luego haz un INSERT para asignar Oxígeno (id=1) a Ana (id=1). Finalmente, haz un JOIN para mostrar el nombre del tripulante y el recurso asignado.",
      "dificultad": "Difícil",
      "tema_sql": "JOIN"
    },
    {
      "id_nivel": 11,
      "titulo": "Encender motores principales",
      "descripcion": "Los motores requieren al menos 300 unidades de Combustible. Actualiza la tabla recursos para reducir el combustible a 200 (simulando el consumo inicial).",
      "dificultad": "Medio",
      "tema_sql": "UPDATE"
    },
    {
      "id_nivel": 12,
      "titulo": "Expulsar carga dañada",
      "descripcion": "Se detectó un contenedor roto de Oxígeno contaminado. Elimínalo de la tabla recursos.",
      "dificultad": "Medio",
      "tema_sql": "DELETE"
    },
    {
      "id_nivel": 13,
      "titulo": "Crear tabla de coordenadas",
      "descripcion": "Antes de registrar coordenadas debemos crear la estructura. Crea la tabla 'coordenadas' con columnas: id SERIAL PRIMARY KEY, planeta VARCHAR(50), sector VARCHAR(50).",
      "dificultad": "Fácil",
      "tema_sql": "CREATE TABLE"
    },
    {
      "id_nivel": 14,
      "titulo": "Insertar coordenadas de despegue",
      "descripcion": "Inserta en 'coordenadas' el punto de despegue inicial: ('Alpha Centauri', 'Sector 7G').",
      "dificultad": "Fácil",
      "tema_sql": "INSERT"
    },
    {
      "id_nivel": 15,
      "titulo": "Verificar sistemas críticos",
      "descripcion": "Crea una consulta que muestre todos los tripulantes y los recursos que tienen asignados (JOIN entre tripulacion, asignaciones y recursos).",
      "dificultad": "Difícil",
      "tema_sql": "JOIN"
    },
    {
      "id_nivel": 16,
      "titulo": "¡Despegue!",
      "descripcion": "La nave está lista para despegar. Inserta en la tabla 'coordenadas' el destino final: ('Nebulosa de Orión','Sector X9'). Luego haz un SELECT para listar todas las coordenadas registradas.",
      "dificultad": "Medio",
      "tema_sql": "SELECT"
    }
  ]
```

- JSON MISIONES usa el ENDPOINT /misiones/bulk_create:
```bash

  [
    {
      "id_nivel": 1,
      "enunciado": "Crea la base de datos 'nave_estrella'.",
      "consulta_correcta": "CREATE DATABASE nave_estrella;",
      "tabla_base": ""
    },
    {
      "id_nivel": 2,
      "enunciado": "Crea la tabla 'tripulacion' con columnas: id SERIAL PRIMARY KEY, nombre VARCHAR(50), rol VARCHAR(50).",
      "consulta_correcta": "CREATE TABLE tripulacion (id SERIAL PRIMARY KEY, nombre VARCHAR(50), rol VARCHAR(50));",
      "tabla_base": ""
    },
    {
      "id_nivel": 3,
      "enunciado": "Inserta los tripulantes iniciales en tripulacion: (Ana, Piloto), (José, Ingeniero), (Luisa, Médica).",
      "consulta_correcta": "INSERT INTO tripulacion (nombre, rol) VALUES ('Ana','Piloto'), ('José','Ingeniero'), ('Luisa','Médica');",
      "tabla_base": "tripulacion"
    },
    {
      "id_nivel": 4,
      "enunciado": "Selecciona id, nombre y rol de todos los tripulantes.",
      "consulta_correcta": "SELECT id, nombre, rol FROM tripulacion;",
      "tabla_base": "tripulacion"
    },
    {
      "id_nivel": 5,
      "enunciado": "Elimina al tripulante con nombre 'José'.",
      "consulta_correcta": "DELETE FROM tripulacion WHERE nombre = 'José';",
      "tabla_base": "tripulacion"
    },
    {
      "id_nivel": 6,
      "enunciado": "Actualiza el rol de Luisa a 'Comandante'.",
      "consulta_correcta": "UPDATE tripulacion SET rol = 'Comandante' WHERE nombre = 'Luisa';",
      "tabla_base": "tripulacion"
    },
    {
      "id_nivel": 7,
      "enunciado": "Crea la tabla 'recursos' con columnas: id SERIAL PRIMARY KEY, tipo VARCHAR(50), cantidad INT.",
      "consulta_correcta": "CREATE TABLE recursos (id SERIAL PRIMARY KEY, tipo VARCHAR(50), cantidad INT);",
      "tabla_base": ""
    },
    {
      "id_nivel": 8,
      "enunciado": "Inserta en recursos: (Oxígeno, 100), (Combustible, 500), (Agua, 200).",
      "consulta_correcta": "INSERT INTO recursos (tipo, cantidad) VALUES ('Oxígeno',100), ('Combustible',500), ('Agua',200);",
      "tabla_base": "recursos"
    },
    {
      "id_nivel": 9,
      "enunciado": "Selecciona los recursos con cantidad < 300.",
      "consulta_correcta": "SELECT tipo, cantidad FROM recursos WHERE cantidad < 300;",
      "tabla_base": "recursos"
    },
    {
      "id_nivel": 10,
      "enunciado": "Crea 'asignaciones', inserta Oxígeno (id=1) a Ana (id=1), y haz un JOIN para mostrar nombre y recurso.",
      "consulta_correcta": "SELECT t.nombre, r.tipo FROM asignaciones a JOIN tripulacion t ON a.tripulante_id = t.id JOIN recursos r ON a.recurso_id = r.id;",
      "tabla_base": "asignaciones"
    },
    {
      "id_nivel": 11,
      "enunciado": "Actualiza el combustible a 200 unidades.",
      "consulta_correcta": "UPDATE recursos SET cantidad = 200 WHERE tipo = 'Combustible';",
      "tabla_base": "recursos"
    },
    {
      "id_nivel": 12,
      "enunciado": "Elimina el recurso 'Oxígeno'.",
      "consulta_correcta": "DELETE FROM recursos WHERE tipo = 'Oxígeno';",
      "tabla_base": "recursos"
    },
    {
      "id_nivel": 13,
      "enunciado": "Crea la tabla 'coordenadas' con columnas: id SERIAL PRIMARY KEY, planeta VARCHAR(50), sector VARCHAR(50).",
      "consulta_correcta": "CREATE TABLE coordenadas (id SERIAL PRIMARY KEY, planeta VARCHAR(50), sector VARCHAR(50));",
      "tabla_base": ""
    },
    {
      "id_nivel": 14,
      "enunciado": "Inserta coordenada inicial ('Alpha Centauri','Sector 7G').",
      "consulta_correcta": "INSERT INTO coordenadas (planeta, sector) VALUES ('Alpha Centauri','Sector 7G');",
      "tabla_base": "coordenadas"
    },
    {
      "id_nivel": 15,
      "enunciado": "Haz un JOIN para mostrar tripulantes y recursos asignados.",
      "consulta_correcta": "SELECT t.nombre, r.tipo FROM asignaciones a JOIN tripulacion t ON a.tripulante_id = t.id JOIN recursos r ON a.recurso_id = r.id;",
      "tabla_base": "asignaciones"
    },
    {
      "id_nivel": 16,
      "enunciado": "Inserta coordenada ('Nebulosa de Orión','Sector X9') y selecciona todas las coordenadas.",
      "consulta_correcta": "SELECT * FROM coordenadas;",
      "tabla_base": "coordenadas"
    }
  ]
```

- JSON LOGROS usa el ENDPOINT /logross/create (tendras que ingresar 1 x1):
```bash
[
  {
    "nombre": "Primeros pasos en SQL",
    "descripcion": "Completaste tu primera misión en el nivel 1",
  },
  {
    "nombre": "Explorador de datos",
    "descripcion": "Completaste todas las misiones del nivel 1",
  },
  {
    "nombre": "Consultor avanzado",
    "descripcion": "Completaste todas las misiones del nivel 2",
  },
  {
    "nombre": "Dominador de niveles",
    "descripcion": "Completaste todas las misiones de todos los niveles",
  },
  {
    "nombre": "Persistente",
    "descripcion": "Intentaste 10 veces resolver misiones aunque te equivocaste",
  },
  {
    "nombre": "Velocidad SQL",
    "descripcion": "Completaste una misión en menos de 1 minuto",
  }
]
```