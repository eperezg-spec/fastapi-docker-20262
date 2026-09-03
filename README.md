# Servicio de cedulas con FastAPI

Servicio web que devuelve un numero entero aleatorio de exactamente 10 digitos.

## API

### Obtener una cedula

```http
GET /obtener_cedula
```

No requiere parametros ni body.

Payload de respuesta exitoso (`200 OK`):

```json
1234567890
```

El valor siempre es un entero entre `1000000000` y `9999999999`.

Ejemplo con `curl`:

```powershell
curl http://localhost:8000/obtener_cedula
```

### Obtener numero romano

```http
GET /obtener_numero_romano
```

No requiere parametros ni body. Devuelve aleatoriamente la representacion romana de un numero entre 50 y 100.

Payload de respuesta exitoso (`200 OK`):

```json
"LXXXIV"
```

Ejemplo con `curl`:

```powershell
curl http://localhost:8000/obtener_numero_romano
```

### Duplicar un numero

```http
GET /duplicar_numero?numero=7
```

Recibe un numero entero mediante el parametro `numero` y devuelve el mismo valor multiplicado por 2.

Payload de respuesta exitoso (`200 OK`):

```json
14
```

Ejemplo con `curl`:

```powershell
curl "http://localhost:8000/duplicar_numero?numero=7"
```

## Swagger y OpenAPI

Con el servicio levantado, abre:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Especificacion OpenAPI: http://localhost:8000/openapi.json
- Swagger estatico: [swagger.html](swagger.html), abrible directamente en el navegador

El archivo `swagger.html` incluye la documentacion del endpoint y funciona como una pagina independiente usando Swagger UI desde CDN.

## Docker Compose

Requisitos: Docker Desktop iniciado.

Construir la imagen y levantar el servicio:

```powershell
docker compose up --build
```

El servicio queda disponible en http://localhost:8000.

Ejecutarlo en segundo plano:

```powershell
docker compose up --build -d
```

Ver logs:

```powershell
docker compose logs -f api
```

Detener y eliminar el contenedor:

```powershell
docker compose down
```

## Coleccion Postman

Importa [`postman_collection.json`](postman_collection.json) en Postman.

La coleccion incluye las peticiones `GET /obtener_cedula`, `GET /obtener_numero_romano` y `GET /duplicar_numero`, con pruebas automaticas para validar sus respuestas.

## Ejecucion local sin Docker

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Docker sin Compose

```powershell
docker build -t servicio-cedula .
docker run --rm -p 8000:8000 servicio-cedula
```

## Despliegue continuo en GitHub Actions y Render

El workflow [`deploy.yml`](.github/workflows/deploy.yml) se ejecuta automaticamente en cada `push` a la rama `main`. Realiza estas acciones:

1. Instala Python y las dependencias.
2. Valida que se generen cedulas enteras de 10 digitos.
3. Construye la imagen Docker.
4. Solicita un nuevo despliegue en Render mediante un Deploy Hook.

### Configurar Render Free

1. Sube este proyecto a un repositorio de GitHub.
2. En Render, selecciona **New > Web Service** y conecta el repositorio.
3. Selecciona **Docker** como runtime.
4. Define el plan **Free** y crea el servicio.
5. En **Settings > Deploy Hook**, crea un hook y copia su URL.
6. En GitHub abre **Settings > Secrets and variables > Actions > New repository secret**.
7. Crea el secreto `RENDER_DEPLOY_HOOK` y pega la URL del hook.
8. Ejecuta el workflow desde **Actions > CI/CD - Servicio de cedulas > Run workflow**, o haz push a `main`.

Render construira el `Dockerfile` y asignara automaticamente la variable `PORT`. El contenedor ya esta preparado para escuchar ese puerto.

Tambien puedes crear el servicio desde el Blueprint [`render.yaml`](render.yaml), seleccionando **New > Blueprint** en Render. El archivo deja `autoDeploy: false` para que los despliegues queden controlados por GitHub Actions mediante el Deploy Hook.

Cuando el despliegue termine, Render mostrara una URL similar a:

```text
https://servicio-cedula.onrender.com
```

Endpoints publicados:

- API: `https://servicio-cedula.onrender.com/obtener_cedula`
- Swagger: `https://servicio-cedula.onrender.com/docs`
- ReDoc: `https://servicio-cedula.onrender.com/redoc`
- OpenAPI: `https://servicio-cedula.onrender.com/openapi.json`

En el plan gratuito, el servicio puede quedar suspendido despues de un periodo de inactividad y tardar unos segundos en responder al primer request.
