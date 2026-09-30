def validar_productos(productos):
    if not productos:
        raise ValueError("La venta debe incluir al menos un producto.")

    for producto in productos:
        if producto["precio"] <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if producto["cantidad"] <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")


def calcular_subtotal(productos):
    return round(
        sum(producto["precio"] * producto["cantidad"]
            for producto in productos),
        2
    )


def calcular_descuento(subtotal):
    # Se aplica un 10% de descuento en compras de $1,000 o más.
    if subtotal >= 1000:
        return round(subtotal * 0.10, 2)

    return 0.0


def mostrar_ticket(productos, subtotal, descuento, iva, total):
    print("=" * 60)
    print("                 TIENDA TECNO IDSM41")
    print("                   REPORTE DE VENTA")
    print("=" * 60)

    print(f"{'Producto':<20}{'Cant.':>6}{'Precio':>15}{'Importe':>15}")
    print("-" * 60)

    for producto in productos:
        importe = producto["precio"] * producto["cantidad"]

        print(
            f"{producto['nombre']:<20}"
            f"{producto['cantidad']:>6}"
            f"{producto['precio']:>15.2f}"
            f"{importe:>15.2f}"
        )

    print("-" * 60)
    print(f"Subtotal:                  ${subtotal:>10.2f}")
    print(f"Descuento:                 ${descuento:>10.2f}")
    print(f"IVA (16%):                 ${iva:>10.2f}")
    print(f"TOTAL A PAGAR:             ${total:>10.2f}")
    print("=" * 60)
    print("Moneda: pesos mexicanos (MXN)")


def mostrar_estadisticas(productos):
    unidades = sum(producto["cantidad"] for producto in productos)

    mayor_importe = max(
        productos,
        key=lambda producto: producto["precio"] * producto["cantidad"]
    )

    print("\nESTADISTICAS DE LA VENTA")
    print(f"Productos diferentes: {len(productos)}")
    print(f"Unidades vendidas: {unidades}")
    print(f"Producto con mayor importe: {mayor_importe['nombre']}")


def main():
    productos = [
        {"nombre": "Teclado", "precio": 350.00, "cantidad": 2},
        {"nombre": "Mouse", "precio": 180.00, "cantidad": 3},
        {"nombre": "Memoria USB", "precio": 120.00, "cantidad": 4},
        {"nombre": "Audifonos", "precio": 450.00, "cantidad": 1},
        {"nombre": "Cable HDMI", "precio": 150.00, "cantidad": 2},
    ]

    validar_productos(productos)

    subtotal = calcular_subtotal(productos)
    descuento = calcular_descuento(subtotal)
    base = subtotal - descuento

    # Para este ejemplo, los precios no incluyen IVA.
    iva = round(base * 0.16, 2)
    total = round(base + iva, 2)

    mostrar_ticket(productos, subtotal, descuento, iva, total)
    mostrar_estadisticas(productos)

    print("\nPrograma finalizado correctamente.")


if __name__ == "__main__":
    main()
