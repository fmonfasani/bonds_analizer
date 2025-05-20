from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

FRECUENCIAS = {
    "anual": 1,
    "semestral": 2,
    "trimestral": 4
}

def generar_fechas_pago(fecha_emision, fecha_vto, frecuencia):
    pagos = []
    meses = 12 // FRECUENCIAS.get(frecuencia.lower(), 1)
    fecha = fecha_emision

    while fecha < fecha_vto:
        fecha += relativedelta(months=meses)
        if fecha <= fecha_vto:
            pagos.append(fecha)

    pagos.append(fecha_vto)
    return pagos

def generar_cashflows(nominal, tasa_anual, frecuencia, fecha_emision, fecha_vto):
    frecuencia = frecuencia.lower()
    fechas = generar_fechas_pago(fecha_emision, fecha_vto, frecuencia)
    n_cupones = FRECUENCIAS.get(frecuencia, 1)
    tasa_periodica = tasa_anual / 100 / n_cupones
    cupon = round(nominal * tasa_periodica, 2)

    flujos = []
    for i, fecha in enumerate(fechas):
        monto = cupon
        if i == len(fechas) - 1:
            monto += nominal  # último pago incluye el principal
        flujos.append((fecha, monto))

    return flujos
