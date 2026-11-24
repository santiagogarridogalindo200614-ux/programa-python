"""
Santiago Garrido Galindo
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación (213022)
Problema 2: Menú de restaurante con promoción
"""

# ---------------------------------------------------------
# Constantes de la promoción (definidas previamente)
# ---------------------------------------------------------
CATEGORIA_OBJETIVO = "Platos fuertes"
UMBRAL_PRECIO = 20000
PORCENTAJE_DESCUENTO = 0.15  # 15 %

# ---------------------------------------------------------
# Matriz del menú: [Nombre del producto, Categoría, Precio base]
# ---------------------------------------------------------
menu = [
    ["Bandeja paisa", "Platos fuertes", 32000],
    ["Salmón a la plancha", "Platos fuertes", 45000],
    ["Hamburguesa clásica", "Platos fuertes", 18000],
    ["Sopa de verduras", "Entradas", 12000],
    ["Limonada de coco", "Bebidas", 9000],
    ["Tres leches", "Postres", 11000],
    ["Brownie con helado", "Postres", 15000],
]


# ---------------------------------------------------------
# Función: calcula el precio final de un producto
# ---------------------------------------------------------
def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):
    """
    Aplica 15 % de descuento si el producto es de la categoría objetivo
    Y su precio base es mayor al umbral. Si no, devuelve el precio base.
    """
    if categoria == categoria_objetivo and precio_base > umbral:
        return precio_base - (precio_base * PORCENTAJE_DESCUENTO)
    return precio_base


# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    print("=" * 62)
    print("        MENÚ CON PROMOCIÓN - RESTAURANTE")
    print("=" * 62)
    print(f"Promoción: {int(PORCENTAJE_DESCUENTO * 100)}% en '{CATEGORIA_OBJETIVO}' "
          f"con precio base mayor a ${UMBRAL_PRECIO:,}")
    print("-" * 62)
    print(f"{'Producto':<24}{'Precio base':>14}{'Precio final':>16}")
    print("-" * 62)

    for fila in menu:
        nombre = fila[0]
        categoria = fila[1]
        precio_base = fila[2]

        precio_final = calcular_precio_final(
            categoria, precio_base, CATEGORIA_OBJETIVO, UMBRAL_PRECIO
        )

        marca = "  <- promoción" if precio_final < precio_base else ""
        print(f"{nombre:<24}{'$' + format(precio_base, ',.0f'):>14}"
              f"{'$' + format(precio_final, ',.0f'):>16}{marca}")

    print("=" * 62)


main()