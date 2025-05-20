import re
from datetime import datetime

def extract_bono_data(texto: str) -> dict:
    data = {}

    # Emisor
    match_emisor = re.search(r"(?:Issuer|Emisor)[:\s\-]+(.+)", texto, re.IGNORECASE)
    if match_emisor:
        data["emisor"] = match_emisor.group(1).strip()

    # Vencimiento
    match_vto = re.search(r"(?:Maturity Date|Vencimiento)[:\s\-]+([A-Za-z]+\s\d{1,2},?\s\d{4})", texto, re.IGNORECASE)
    if match_vto:
        try:
            data["vencimiento"] = datetime.strptime(match_vto.group(1).replace(",", ""), "%B %d %Y").date().isoformat()
        except:
            data["vencimiento"] = match_vto.group(1).strip()

    # Tasa
    match_tasa = re.search(r"(?:Interest Rate|Coupon Rate|Tasa)[:\s\-]+([\d.]+)%", texto, re.IGNORECASE)
    if match_tasa:
        data["tasa"] = float(match_tasa.group(1))

    # Frecuencia
    if re.search("quarterly", texto, re.IGNORECASE):
        data["frecuencia"] = "trimestral"
    elif re.search("semiannual", texto, re.IGNORECASE):
        data["frecuencia"] = "semestral"
    elif re.search("annual", texto, re.IGNORECASE):
        data["frecuencia"] = "anual"
    else:
        data["frecuencia"] = "desconocida"

    # CUSIP
    match_cusip = re.search(r"CUSIP[:\s\-]+([A-Z0-9]{8,})", texto)
    if match_cusip:
        data["cusip"] = match_cusip.group(1)

    # ISIN
    match_isin = re.search(r"ISIN[:\s\-]+([A-Z]{2}[A-Z0-9]{9}[0-9])", texto)
    if match_isin:
        data["isin"] = match_isin.group(1)

    # Subyacentes (opcional, simplificado)
    match_suby = re.search(r"Underlying assets?[:\s\-]+(.+)", texto, re.IGNORECASE)
    if match_suby:
        data["subyacentes"] = match_suby.group(1).split(",")

    return data
