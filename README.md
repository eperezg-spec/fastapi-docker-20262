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

La coleccion incluye la peticion `GET /obtener_cedula` y una prueba que valida que la respuesta sea un entero de 10 digitos.

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
