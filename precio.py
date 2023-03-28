#precio
nombre_producto, codigo = input("Ingrese nombre y codigo del producto : ").split()
costo_produccion = float(input("INGRESE COSTO DE PRODUCCION "))
#calculos
utilidad = costo_produccion * 1.2
impuesto = costo_produccion * 0.15

precio_venta = costo_produccion + utilidad + impuesto

print (f"El producto {nombre_producto} y codigo {codigo}\
    tiene un precio de venta {precio_venta:.2f}")