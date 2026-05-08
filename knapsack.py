"""
Problema 2 — Knapsack Fraccionado
Paradigma: Greedy
"""


def knapsack_fraccionado(articulos: list[dict], W: float) -> tuple[float, list]:

    # Calcular densidad de cada articulo
    for a in articulos:
        a['densidad'] = a['precio'] / a['peso']

    # Ordenar por densidad descendente (criterio greedy)
    articulos_ord = sorted(articulos, key=lambda x: x['densidad'], reverse=True)

    valor_total = 0.0
    seleccion = []
    capacidad = W

    for a in articulos_ord:
        if capacidad <= 0:
            break
        cantidad = min(a['peso'], capacidad)
        valor = cantidad * a['densidad']
        seleccion.append({
            'nombre': a['nombre'],
            'cantidad': cantidad,
            'valor': valor
        })
        valor_total += valor
        capacidad -= cantidad

    return valor_total, seleccion


def imprimir_resultado(articulos: list[dict], W: float) -> None:
    valor, seleccion = knapsack_fraccionado(articulos, W)

    print(f"Capacidad W = {W} u")
    print(f"{'Articulo':<14} {'Peso':>6} {'Precio':>8} {'Densidad':>10} "
          f"{'Tomado':>8} {'Valor':>10}")
    print("-" * 62)

    densidades = {a['nombre']: a['densidad'] for a in articulos}
    pesos      = {a['nombre']: a['peso']     for a in articulos}
    precios    = {a['nombre']: a['precio']   for a in articulos}

    for s in seleccion:
        n = s['nombre']
        print(f"{n:<14} {pesos[n]:>6.1f} {precios[n]:>8.1f} "
              f"{densidades[n]:>10.4f} {s['cantidad']:>8.1f} {s['valor']:>10.2f}")

    print("-" * 62)
    print(f"{'VALOR TOTAL':>52} {valor:>10.2f}")
    print()


if __name__ == "__main__":
    print("=" * 62)
    print("CASO 1 — Ejemplo del PDF")
    print("Items: (w=10,$60), (w=20,$100), (w=30,$120)  W=50")
    print("Esperado: 10u item1 + 20u item2 + 20u item3 = $240")
    print("=" * 62)
    caso1 = [
        {'nombre': 'item 1', 'peso': 10, 'precio': 60},
        {'nombre': 'item 2', 'peso': 20, 'precio': 100},
        {'nombre': 'item 3', 'peso': 30, 'precio': 120},
    ]
    imprimir_resultado(caso1, W=50)

    print("=" * 62)
    print("CASO 2 — Solo cabe fraccion del mejor item")
    print("Items: oro(w=5,$500), plata(w=10,$600), bronce(w=15,$300)  W=12")
    print("=" * 62)
    caso2 = [
        {'nombre': 'oro',    'peso': 5,  'precio': 500},
        {'nombre': 'plata',  'peso': 10, 'precio': 600},
        {'nombre': 'bronce', 'peso': 15, 'precio': 300},
    ]
    imprimir_resultado(caso2, W=12)

    print("=" * 62)
    print("CASO 3 — Mochila mayor que suma de todos los pesos")
    print("Items: A(w=3,$30), B(w=4,$40), C(w=5,$45)  W=20")
    print("Esperado: se toman todos los items completos")
    print("=" * 62)
    caso3 = [
        {'nombre': 'A', 'peso': 3, 'precio': 30},
        {'nombre': 'B', 'peso': 4, 'precio': 40},
        {'nombre': 'C', 'peso': 5, 'precio': 45},
    ]
    imprimir_resultado(caso3, W=20)

    print("=" * 62)
    print("CASO 4 — Un solo item, mayor que la mochila (fraccion pura)")
    print("Items: diamante(w=100,$1000)  W=40")
    print("=" * 62)
    caso4 = [
        {'nombre': 'diamante', 'peso': 100, 'precio': 1000},
    ]
    imprimir_resultado(caso4, W=40)
