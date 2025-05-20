from datetime import date
from cashflows import generar_cashflows
from duration import calcular_duracion, calcular_convexidad

nominal = 1000
tasa = 12.5
frecuencia = "trimestral"
fecha_emision = date(2024, 11, 19)
fecha_vto = date(2026, 11, 18)
tir = 13.92  # desde el módulo TIR

flujos = generar_cashflows(nominal, tasa, frecuencia, fecha_emision, fecha_vto)

dur_mac, dur_mod = calcular_duracion(flujos, tir)
convexidad = calcular_convexidad(flujos, tir)

print(f"Duración Macaulay: {dur_mac} años")
print(f"Duración Modificada: {dur_mod} años")
print(f"Convexidad: {convexidad}")
