"""
Problema 3 — Combinaciones de n digitos en teclado Nokia 3230
Paradigma: Programacion Dinamica (bottom-up)
"""

VECINOS = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [2, 1, 3, 5],
    3: [3, 2, 6],
    4: [4, 1, 5, 7],
    5: [5, 2, 4, 6, 8],
    6: [6, 3, 5, 9],
    7: [7, 4, 8],
    8: [8, 5, 7, 9, 0],
    9: [9, 6, 8],
}


def contar_combinaciones(n: int) -> int:
    """Retorna el total de combinaciones validas de longitud n."""
    if n <= 0:
        return 0

    # Caso base: f(1, d) = 1 para todo d
    dp = [1] * 10

    for _ in range(2, n + 1):
        dp_nuevo = [0] * 10
        for d in range(10):
            for v in VECINOS[d]:
                dp_nuevo[d] += dp[v]
        dp = dp_nuevo

    return sum(dp)


def mostrar_detalle(n: int) -> None:
    """Muestra la tabla DP paso a paso y el total."""
    if n <= 0:
        print("n debe ser >= 1")
        return

    dp = [1] * 10
    print(f"\n{'k':>3} | " + " ".join(f"d={d}" for d in range(10)) + " | Total")
    print("-" * 70)
    print(f"{'1':>3} | " + " ".join(f"{v:5}" for v in dp) + f" | {sum(dp)}")

    for k in range(2, n + 1):
        dp_nuevo = [0] * 10
        for d in range(10):
            for v in VECINOS[d]:
                dp_nuevo[d] += dp[v]
        dp = dp_nuevo
        print(f"{k:>3} | " + " ".join(f"{v:5}" for v in dp) + f" | {sum(dp)}")

    print()


if __name__ == "__main__":
    print("=" * 70)
    print("CASO 1 — n=1 (cualquier digito individualmente)")
    print("Esperado: 10  (un dígito por cada tecla 0-9)")
    print("=" * 70)
    mostrar_detalle(1)
    print(f"Total combinaciones n=1: {contar_combinaciones(1)}\n")

    print("=" * 70)
    print("CASO 2 — n=2 (verificacion con el PDF)")
    print("Esperado: 36")
    print("=" * 70)
    mostrar_detalle(2)
    resultado_n2 = contar_combinaciones(2)
    print(f"Total combinaciones n=2: {resultado_n2}")
    assert resultado_n2 == 36, f"ERROR: esperado 36, obtenido {resultado_n2}"
    print("Verificacion correcta: 36\n")

    print("=" * 70)
    print("CASO 3 — n=3")
    print("=" * 70)
    mostrar_detalle(3)
    print(f"Total combinaciones n=3: {contar_combinaciones(3)}\n")

    print("=" * 70)
    print("CASO 4 — n=5")
    print("=" * 70)
    mostrar_detalle(5)
    print(f"Total combinaciones n=5: {contar_combinaciones(5)}\n")

    print("=" * 70)
    print("CASO 5 — n=10 (caso no trivial grande)")
    print("=" * 70)
    print(f"Total combinaciones n=10: {contar_combinaciones(10)}\n")
