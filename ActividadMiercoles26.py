ARROZ = float(0.125)
MARISCOS = float(0.0625)
Precio_Arroz_Para_1 = float(100)
Precio_Mariscos_Para_1 = float(200) 
PAELLA1 = (ARROZ + MARISCOS)
Comensales = int(input("Ingresar comensales: "))
if PAELLA1 * Comensales:
    print ("Cantidad de arroz a utilizar: ", ARROZ * Comensales, "Kilogramos")
    print("Cantidad de mariscos a utilizar: ", MARISCOS * Comensales, "Kilogramos")
    print("Precio del Arroz", Precio_Arroz_Para_1 * Comensales, "ARS")
    print("Precio de los Mariscos", Precio_Mariscos_Para_1 * Comensales, "ARS")