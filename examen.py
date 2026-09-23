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
d = 10000
c_total_productos = int(0)
c_a = int(0)
c_al = int(0)
c_t = int(0)
d_g=int(0)
# Crear las listas de productos y precios.
l_productos = ["Agua", "Alfajor", "Tostada"]
l_precios = [700, 900, 2200]
# Pedir los datos del cliente.
nombre_comprador = input("Ingrese su nombre completo: ")
d = int(input("Ingrese cuanto dinero tiene disponible: "))
print("INTEFAZ KIOSCO:")
print(f"Nombre del comprador:", nombre_comprador)
print(f"Dinero disponible:", d)
print(f"Binvendo", nombre_comprador)
print(f"Tiene", d, "pesos para gastar")

# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
print("productos disponibles:")
for I in range(0, 3):
    a=I
    print(f"-",l_productos [a], ":", l_precios [I])
p_e = input("Elija un producto(para agua presione 1, para alfajor 2 y para tostada 3)")
if p_e == "1":
    if d>700:
        d=d-700
        d_g=d_g+700
        c_total=c_total+1
        c_a=c_a+1
elif p_e == "2":
     if d>900:
        d=d-900
        d_g=d_g+900
        c_total=c_total+1
        c_al=c_al+1
elif p_e == "2":
     if d>2200:
        d=d-2200
        d_g=d_g+2200
        c_total=c_total+1
        c_t=c_t+1
else:
    print("Saldo insuficiente")
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
