from datetime import date

def calcular_tir(flujos, precio, guess=0.05, max_iter=100, tol=1e-6):
    """
    Calcula la TIR dada una lista de flujos (fecha, monto) y el precio del bono.
    """

    def f(tir):
        return sum([
            monto / (1 + tir) ** ((fecha - flujos[0][0]).days / 365)
            for fecha, monto in flujos
        ]) - precio

    def df(tir):
        return sum([
            -((fecha - flujos[0][0]).days / 365) * monto / (1 + tir) ** (((fecha - flujos[0][0]).days / 365) + 1)
            for fecha, monto in flujos
        ])

    tir = guess
    for _ in range(max_iter):
        valor = f(tir)
        derivada = df(tir)

        if derivada == 0:
            return None  # no converge

        nuevo_tir = tir - valor / derivada

        if abs(nuevo_tir - tir) < tol:
            return round(nuevo_tir * 100, 4)  # % anual

        tir = nuevo_tir

    return None  # no converge
