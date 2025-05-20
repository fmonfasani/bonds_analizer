from datetime import date
from cashflows import generar_cashflows
from tir import calcular_tir

nominal = 1000
precio_mercado = 980
tasa = 12.5
frecuencia = "trimestral"
fecha_emision = date(2024, 11, 19)
fecha_vto = date(2026, 11, 18)

flujos = generar_cashflows(nominal, tasa, frecuencia, fecha_emision, fecha_vto)
tir = calcular_tir(flujos, precio_mercado)

print(f"TIR estimada: {tir}%")
