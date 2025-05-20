from datetime import date

def calcular_duracion(flujos, tir_anual):
    """
    Calcula duración de Macaulay y duración modificada.
    flujos: lista de (fecha, monto)
    tir_anual: tasa anual efectiva (%)
    """

    tir = tir_anual / 100
    fecha_base = flujos[0][0]

    valor_presente_total = 0
    suma_tiempo_vp = 0

    for fecha, monto in flujos:
        t = (fecha - fecha_base).days / 365
        vp = monto / (1 + tir) ** t
        valor_presente_total += vp
        suma_tiempo_vp += t * vp

    if valor_presente_total == 0:
        return None, None

    dur_macaulay = suma_tiempo_vp / valor_presente_total
    dur_modificada = dur_macaulay / (1 + tir)

    return round(dur_macaulay, 4), round(dur_modificada, 4)

def calcular_convexidad(flujos, tir_anual):
    tir = tir_anual / 100
    fecha_base = flujos[0][0]

    convexidad_numerador = 0
    valor_presente_total = 0

    for fecha, monto in flujos:
        t = (fecha - fecha_base).days / 365
        vp = monto / (1 + tir) ** t
        valor_presente_total += vp
        convexidad_numerador += t * (t + 1) * vp

    convexidad = convexidad_numerador / ((1 + tir) ** 2 * valor_presente_total)
    return round(convexidad, 4)
