import streamlit as st
from datetime import date
from extractor import extract_bono_data
from cashflows import generar_cashflows
from tir import calcular_tir
from duration import calcular_duracion, calcular_convexidad

st.set_page_config(page_title="📊 Analizador de Bonos", layout="centered")
st.title("📈 Comparador Técnico de Bonos")

st.markdown("Subí un archivo de texto limpio con los datos del bono (extraídos del prospecto) y obtené un análisis automático.")

uploaded_file = st.file_uploader("📎 Subí el archivo .txt", type=["txt"])

if uploaded_file:
    texto = uploaded_file.read().decode("utf-8")
    bono = extract_bono_data(texto)

    if not bono:
        st.error("No se pudo extraer información clave del prospecto. Verificá el formato del texto.")
    else:
        st.subheader("🧾 Datos extraídos")
        st.json(bono)

        st.markdown("---")
        st.subheader("🔢 Parámetros de simulación")
        nominal = st.number_input("💵 Valor nominal", value=1000)
        precio = st.number_input("🏷️ Precio de mercado", value=980.0)

        fecha_emision = date.today()
        fecha_vto = date.fromisoformat(bono.get("vencimiento"))

        flujos = generar_cashflows(
            nominal,
            bono.get("tasa", 0),
            bono.get("frecuencia", "anual"),
            fecha_emision,
            fecha_vto
        )

        st.subheader("📆 Flujos de pago")
        for f in flujos:
            st.text(f"{f[0]}: ${f[1]}")

        tir = calcular_tir(flujos, precio)
        dur_mac, dur_mod = calcular_duracion(flujos, tir)
        convexidad = calcular_convexidad(flujos, tir)

        st.markdown("---")
        st.subheader("📊 Métricas técnicas")
        st.metric("TIR (%)", tir)
        st.metric("Duración Macaulay (años)", dur_mac)
        st.metric("Duración Modificada (años)", dur_mod)
        st.metric("Convexidad", convexidad)

        st.success("✅ Análisis completado con éxito")
