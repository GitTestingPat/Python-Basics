item_1 = 332       # Precio del primer artículo
item_2 = 8912      # Precio del segundo artículo
item_3 = 999       # Precio del tercer artículo

delivery = 2.5     # Porcentaje de costo de envío

# Calcular el importe total
subtotal = (item_1 + item_2 + item_3)  # Suma de los precios de los artículos
shipping_cost = (subtotal * delivery / 100)  # Cálculo del costo de envío
total = subtotal + shipping_cost  # Suma del subtotal y el costo de envío

print(total)
