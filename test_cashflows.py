from datetime import date
from cashflows import generar_cashflows

nominal = 1000
tasa = 12.5  # 12.5% anual
frecuencia = "trimestral"
fecha_emision = date(2024, 11, 19)
fecha_vto = date(2026, 11, 18)

flujos = generar_cashflows(nominal, tasa, frecuencia, fecha_emision, fecha_vto)

for fecha, monto in flujos:
    print(f"{fecha}: ${monto}")
