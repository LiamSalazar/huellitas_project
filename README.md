# Huellitas (Paw Rescue)

## Sistema de Gestión para Refugio de Animales

Sistema web desarrollado en Django + PostgreSQL para gestionar el ciclo completo de rescate, cuidado médico, adopciones y administración de un refugio de animales.

---

## Equipo
- Hernández López Melanie
- Moysen Arcos Angel Eduardo  
- Salazar Martínez Liam Antonio
- Vargas Nicolás Bianca Celeste

---

## Instalación 

### 1. Clonar repositorio
```bash
git clone https://github.com/LiamSalazar/huellitas_project.git
cd huellitas_project/backend

```
### 2. Crear entorno virtual
```bash
python3 -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate   # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos PostgreSQL
```sql
CREATE DATABASE huellitas_db;

CREATE USER huellitas_user WITH PASSWORD 'tu_password';

GRANT ALL PRIVILEGES ON DATABASE huellitas_db TO huellitas_user;
```

### 5. Configurar variables de entorno (Crear archivo .env en /backend)
```env
DEBUG=True

SECRET_KEY=tu_clave_secreta_aqui

DB_NAME=huellitas_db

DB_USER=huellitas_user

DB_PASSWORD=tu_password

DB_HOST=localhost

DB_PORT=5432
```

### 6. Migrar base de datos
```bash
python manage.py migrate
```

### 7. Ejecutar servidor
```bash
python manage.py runserver
```

### 8. Acceder
API: http://localhost:8000/api/

Interfaz: http://localhost:8000/

### Arquitectura

#### Backend 
```txt

apps/

├── users/          # Autenticación y gestión de usuarios

├── animals/        # Registro y gestión de animales

├── adoptions/      # Procesos de adopción

├── finance/        # Módulo financiero (solo administrador)

└── events/         # Gestión de eventos
```

#### Frontend

HTML/CSS/JavaScript puro

Templates Django para renderizado

Interfaces separadas por rol (voluntarios/adoptantes)

---
### Dependencias principales

Django 6.0 + Django REST Framework

PostgreSQL + psycopg2

JWT para autenticación

python-dotenv para configuración

### Pruebas

#### Ejecutar todas las pruebas
```bash
python manage.py test
```

#### Pruebas específicas
```bash
python tests_huellitas.py
```
