# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:Benjamín Lopez Fasanella
# Curso: 2* 2*
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
nombre_comprador="Jaimito"
dinero_compras = 10000
cant_total_productos = int(0)
cant_aguas = int(0)
cant_alfajores = int(0)
cant_tostadas = int(0)
# Crear las listas de productos y precios.
l_productos = ["Agua", "Alfajor", "Tostada"]
l_precios = [700, 900, 2200]
# Pedir los datos del cliente.
nombre_comprador = input("Ingrese su nombre completo: ")
dinero_compras = int(input("Ingrese cuanto dinero tiene disponible: "))
print("INTEFAZ KIOSCO:")
print(f"Nombre del comprador:", nombre_comprador)
print(f"Dinero disponible:", dinero_compras)
print(f"Binvendo", nombre_comprador)
print(f"Tiene", dinero_compras, "pesos para gastar")

# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
print("productos disponibles:")
for I in range(0, 3):
    a=I
    print(f"-",l_productos [a], ":", l_precios [I])
producto_elegido = input()
 
# Utilizar las listas para obtener producto y precio.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
