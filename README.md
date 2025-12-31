# API RESTful con Django e Integración de Spotify

## 📌 Descripción del proyecto

Este repositorio contiene el desarrollo de una **API RESTful completa utilizando Django y Django Rest Framework**, realizada como entrega para la asignatura **Fundamentos de Backend con Python**.

El proyecto implementa un backend capaz de gestionar datos mediante operaciones CRUD y de integrarse con una **API externa (Spotify)** para obtener información sobre canciones y artistas, utilizando autenticación OAuth 2.0.

---

## 🎯 Objetivos del proyecto

* Crear una API RESTful utilizando Django.
* Utilizar **JSON** como formato de intercambio de datos entre cliente y servidor.
* Implementar operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar).
* Integrar la **API de Spotify** para obtener datos musicales.
* Implementar validación de datos y manejo de errores.

---

## 📁 Estructura del proyecto

```
project/
│── spotify/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── util.py
│   └── credentials.py
│── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│── manage.py
```

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd project
```

### 2️⃣ Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install django djangorestframework requests
```

### 4️⃣ Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

---

## 🔐 Configuración de Spotify

1. Crear una aplicación en el **Spotify Developer Dashboard**.
2. Configurar la siguiente Redirect URI:

```
http://localhost:8000/spotify/callback
```

3. Añadir las credenciales en `credentials.py`:

```python
SPOTIFY_CLIENT_ID = "TU_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "TU_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "http://localhost:8000/spotify/callback"
```

---

## 🔗 Endpoints principales

### Autenticación con Spotify

```
GET /spotify/get-auth-url/
```

Devuelve la URL de autorización de Spotify.

### Callback de Spotify

```
GET /spotify/callback
```

Gestiona la autenticación y almacena el token.

### Obtener canciones favoritas

```
GET /spotify/top-tracks/
```

### Obtener artistas favoritos

```
GET /spotify/top-artists/
```

---

## 🧪 Pruebas

Las pruebas de la API se realizaron utilizando **Postman**, verificando:

* Correcto funcionamiento del CRUD
* Autenticación con Spotify
* Obtención de datos de canciones y artistas
* Manejo de errores y respuestas HTTP

---

## ✅ Conclusiones

Este proyecto permitió aplicar de manera práctica los conceptos fundamentales del desarrollo backend, destacando la importancia de una correcta estructuración de la API, el uso de estándares REST y la integración de servicios externos. La práctica ha servido como una base sólida para futuros desarrollos backend más complejos.

---

## 👨‍💻 Autor

Kilian Torres Expósito
M2: Fundamentos de Backend con Python
Universidad Europea
