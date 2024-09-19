# Declaración de variables
precio_total = 0
productos_comprados = int(input("¿Cuántos productos vas a comprar? "))

# Ciclo para procesar cada producto
for i in range(productos_comprados):
    precio_producto = float(input(f"\nIntroduce el precio del producto {i + 1}: $"))
    descuento_producto = float(input("Introduce el porcentaje de descuento: "))
    
    # Calcular el descuento del producto
    descuento_aplicado = (descuento_producto / 100) * precio_producto
    precio_final_producto = precio_producto - descuento_aplicado
    precio_total += precio_final_producto
    
    # Mostrar el precio final de cada producto
    print(f"El precio final del producto {i + 1} después del descuento es: ${precio_final_producto:.2f}")

# Aplicar descuento adicional si hay más de 4 productos
if productos_comprados > 4:
    descuento_adicional = 15
    descuento_extra = (descuento_adicional / 100) * precio_total
    precio_total -= descuento_extra  # Restar el descuento adicional al total
    print(f"\n¡Has comprado más de 4 productos! Se te aplica un descuento adicional del 15%.")
    print(f"Descuento adicional: ${descuento_extra:.2f}")

# Mostrar el total a pagar
print(f"\nEl total a pagar por los {productos_comprados} productos es: ${precio_total:.2f}")



