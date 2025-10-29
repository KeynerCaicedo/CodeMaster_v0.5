-- CodeMaster v0.5 --

CodeMaster es un asistente de desarrollo web enfocado en ayudar a programadores a generar, probar y desplegar código de forma más rápida y estructurada.
Actualmente el proyecto se encuentra en desarrollo activo y documenta paso a paso la evolución del sistema.

Estado actual del proyecto

-- Versión v0.5 (en desarrollo) --

🔹 Se ha estructurado el proyecto en módulos principales:

Frontend → interfaz visual (HTML, CSS, JS o framework correspondiente).

Backend → API construida en Python (posiblemente con FastAPI o Flask).

Tests → pruebas unitarias y funcionales.

🔹 Se está implementando la conexión con PostgreSQL para:

Guardar usuarios registrados.

Persistir el historial de chats.

Manejar sesiones y autenticación de login.

🔹 Uso de Docker para facilitar el despliegue (con Dockerfile y docker-compose.yml).

🔹 Configuración de variables de entorno con .env (no incluidas por seguridad).


-- Requisitos previos --

Para ejecutar el proyecto localmente, asegúrate de tener:
Python 3.10+
Docker
PostgreSQL
Node.js
 (si el frontend usa npm)
Un archivo .env basado en .env.sample


-- Variables de entorno --

Ejemplo de configuración básica (.env.sample):
DATABASE_URL=postgresql://user:password@localhost:5432/codemaster
SECRET_KEY=your_secret_key
DEBUG=True

-- Uso con Docker --

Para levantar el entorno completo:
docker-compose up --build


Esto iniciará:
El contenedor de backend (API Python)
El contenedor de PostgreSQL
(Opcional) El contenedor del frontend

-- Ejecución local (sin Docker) --

Crea y activa un entorno virtual:

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows


Instala dependencias:

pip install -r requirements.txt
Ejecuta el servidor backend:
python backend/main.py
Abre el navegador en:

http://localhost:8000

-- Estructura futura (plan a implementar) --

🔸 Integrar completamente el sistema de autenticación con PostgreSQL.

🔸 Guardar y recuperar historiales de chat desde la base de datos.

🔸 Añadir una interfaz web funcional para interactuar con el backend.

🔸 Implementar migraciones automáticas con Alembic.

🔸 Desplegar el proyecto en la nube (Railway, Render, o AWS).
