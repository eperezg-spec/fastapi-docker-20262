from secrets import randbelow

from fastapi import FastAPI

app = FastAPI(title="Servicio de cedulas")


@app.get("/obtener_cedula", response_model=int)
def obtener_cedula() -> int:
    """Devuelve un numero entero aleatorio de exactamente 10 digitos."""
    return randbelow(9_000_000_000) + 1_000_000_000
