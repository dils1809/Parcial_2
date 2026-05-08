"""
Problema 1 — Hacer sencillo
Paradigma: Greedy
Denominaciones: {1, 5, 10, 25} centavos

Criterio greedy: en cada paso, tomar la mayor denominacion <= monto restante.
"""


def hacer_sencillo(monto_centavos: int) -> tuple[int, dict]:
    """Retorna (total_monedas, {denominacion: cantidad})."""
    denominaciones = [25, 10, 5, 1]
    resultado = {}
    total = 0
    restante = monto_centavos

    for c in denominaciones:
        k = restante // c
        if k > 0:
            resultado[c] = k
            restante -= k * c
            total += k

    return total, resultado


def resolver(monto_quetzales: float) -> None:
    monto_centavos = round(monto_quetzales * 100)
    total, monedas = hacer_sencillo(monto_centavos)

    print(f"Monto   : Q{monto_quetzales:.2f}  ({monto_centavos} centavos)")
    print(f"Monedas : {total} en total")
    for denom in [25, 10, 5, 1]:
        if denom in monedas:
            print(f"  Q{denom/100:.2f} x {monedas[denom]}")
    print()


if __name__ == "__main__":
    print("=" * 45)
    print("CASO 1 — Ejemplo del PDF - Q2.93")
    print("Esperado: 11x Q0.25, 1x Q0.10, 1x Q0.05, 3x Q0.01  - 16 monedas")
    print("=" * 45)
    resolver(2.93)

    print("=" * 45)
    print("CASO 2 — Monto exacto en una denominacion - Q1.00")
    print("Esperado: 4x Q0.25  -4 monedas)")
    print("=" * 45)
    resolver(1.00)

    print("=" * 45)
    print("CASO 3 — Monto que obliga a usar las 4 denominaciones (Q0.41)")
    print("Esperado: 1x Q0.25, 1x Q0.10, 1x Q0.05, 1x Q0.01  (4 monedas)")
    print("=" * 45)
    resolver(0.41)

    print("=" * 45)
    print("CASO 4 — Solo centavos (Q0.06)")
    print("Esperado: 1x Q0.05, 1x Q0.01  (2 monedas)")
    print("=" * 45)
    resolver(0.06)

    print("=" * 45)
    print("CASO 5 — Monto grande (Q9.99)")
    print("=" * 45)
    resolver(9.99)
