# 📊 Bonds Analyzer — Análisis Comparativo de Bonos

Este proyecto permite cargar prospectos de bonos, extraer sus características financieras clave y calcular métricas técnicas como:

- TIR (Tasa Interna de Retorno)
- Duración de Macaulay y Modificada
- Convexidad
- Flujos de fondos proyectados

> Todo esto con una interfaz simple basada en Streamlit y un backend modular escalable en Python.

---

## 🚀 Características

- 📄 Extracción automática de datos desde texto limpio de prospectos
- 🧠 Cálculo completo de métricas técnicas
- 💬 Interfaz web para subir archivos y consultar
- 📈 Compatible con cualquier tipo de bono simple (fijo, bullet, callable)

---

## 📁 Estructura del proyecto

```
bonds_analizer/
├── data/                # Archivos de texto de prospectos
├── parsed/              # (opcional) Resultados estructurados
├── extractor.py         # Extrae emisor, tasa, vencimiento, etc.
├── cashflows.py         # Genera flujos de pago
├── tir.py               # Calcula la TIR efectiva
├── duration.py          # Calcula duración y convexidad
├── app.py               # Interfaz Streamlit
├── test_*.py            # Tests de cada módulo
├── requirements.txt
└── README.md
```

---

## 🛠 Instalación

```bash
pip install -r requirements.txt
```

Agregá tu clave de OpenAI (si usás LLMs para extensión futura) en `.env`:

```
OPENAI_API_KEY=sk-...
```

---

## ▶ Ejecución de la app

```bash
streamlit run app.py
```

1. Subí un archivo `.txt` limpio (extraído de un prospecto de bono)
2. Ingresá el precio actual
3. Recibí:
   - Flujos proyectados
   - TIR
   - Duración Macaulay
   - Duración Modificada
   - Convexidad

---

## 📊 Ejemplo de salida

```
{'emisor': 'Morgan Stanley Finance LLC',
 'vencimiento': '2026-11-18',
 'tasa': 12.98,
 'frecuencia': 'trimestral',
 'cusip': '61776WF81',
 'isin': 'US61776WF814'}

TIR: 16.94%
Duración Macaulay: 1.54 años
Duración Modificada: 1.35 años
Convexidad: 3.19
```

---

## 🧪 Tests unitarios

```bash
python test_cashflows.py
python test_tir.py
python test_duration.py
python test_extractor.py
```

---

## 📬 Autor

Federico Monfasani — 2025

---

## 📄 Licencia

MIT
