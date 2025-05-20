from extractor import extract_bono_data

with open("data/ms_bono_4877.txt", "r", encoding="utf-8") as f:
    texto = f.read()

info = extract_bono_data(texto)
print(info)

