from secrets import randbelow

from fastapi import FastAPI

app = FastAPI(title="Servicio de cedulas")


def convertir_a_romano(numero: int) -> str:
    valores = (
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )
    resultado = []
    restante = numero

    for valor, simbolo in valores:
        cantidad, restante = divmod(restante, valor)
        resultado.append(simbolo * cantidad)

    return "".join(resultado)


@app.get("/obtener_cedula", response_model=int)
def obtener_cedula() -> int:
    """Devuelve un numero entero aleatorio de exactamente 10 digitos."""
    return randbelow(9_000_000_000) + 1_000_000_000


@app.get("/obtener_numero_romano", response_model=str)
def obtener_numero_romano() -> str:
    """Devuelve aleatoriamente un numero romano entre 50 y 100."""
    return convertir_a_romano(randbelow(51) + 50)


@app.get("/duplicar_numero", response_model=int)
def duplicar_numero(numero: int) -> int:
    """Devuelve el numero recibido multiplicado por dos."""
    return numero * 2
