# === PROGRAMA PRINCIPAL === #
import functions as func

# === DICCIONARIOS === #

productos = {
    "8475HD" : ["hp" , 15.6 , "8GB" , "DD" , "1T" , "Intel Core i5" , "Nvidia GTX1050"],
    "2175HD" : ["lenovo" , 14 , "4GB" , "SSD" , "512GB" , "Intel Core i5" , "Nvidia GTX1050"],
    "JjfFHD" : ["asus" , 14 , "16GB" , "SSD" , "256GB" , "Intel Core i7" , "Nvidia GTX2080Ti"],
    "fgdxFHD" : ["hp" , 15.6 , "8GB" , "DD" , "1T" , "Intel Core i3" , "integrada"],
    "GF75HD" : ["asus" , 15.6 , "8GB" , "DD" , "1T" , "Intel Core i7" , "Nvidia GTX1050"],
    "123FHD" : ["lenovo" , 14 , "6GB" , "DD" , "1T" , "AMD Ryzen 5" , "integrada"],
    "342FHD" : ["lenovo" , 15.6 , "8GB" , "DD" , "1T" , "AMD Ryzen 7" , "Nvidia GTX1050"],
    "UWU131HD" : ["Dell" , 15.6 , "8GB" , "DD" , "1T" , "AMD Ryzen 3" , "Nvidia GTX1050"],
    "FS1230HD" : ["lenovo" , 15.6 , "8GB" , "DD" , "1T" , "Intel Core i5" , "Nvidia GTX1050"]
}

stock = {
    "8475HD" : [387990 , 10],
    "2175HD" : [327990 , 4],
    "JjfFHD" : [424990 , 1],
    "fgdxFHD" : [664990 , 21],
    "GF75HD" : [749990 , 2],
    "123FHD" : [290890 , 32],
    "342FHD" : [444990 , 7],
    "UWU131HD" : [349990 , 1],
    "FS1230HD" : [249990 , 0]
}

# === MENÚ PRINCIPAL === #

while True:

    print("\n === ** Tienda Online Pybook ** ===")

    print(""" 
========================
*** MENÚ PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir
========================
    """)

    # === INGRESO DE OPCIONES === #

    while True:

        try:

            opc = int(input("\nIngrese una opción (1-4): "))

            if (opc >= 1 and opc <= 4):

                break
            
            else:

                print("\nERROR: Opción invalida. La opción debe ser un número del 1 al 4")

        except(ValueError):

            print("\nEERROR: Tipo de dato invalido. Debe ser un número entero.")

    # === OPCIONES : === #

    # == Stock por marca == #

    if(opc == 1):

        print("\n== ** Ver Stock por Marca ** ==")

        marca = input ("\nIngrese marca del notebook: ").lower()

        func.stock_marca(marca , productos , stock)

    # == Búsqueda por precio == #

    elif(opc == 2):

        print("\n== ** Búsqueda por precio ** ==")

        while True:

            try:

                p_min = int(input("\nIngrese precio mínimo: "))

                if (p_min > 0):

                    break
                
                else:

                    print("\nERROR: El precio no puede ser un número negativo.")

            except(ValueError):

                print("\nEERROR: Tipo de dato invalido. Debe ser un número entero.")

        while True:

            try:

                p_max = int(input("\nIngrese precio máximo: "))

                if (p_max > 0):

                    break
                
                else:

                    print("\nERROR: El precio no puede ser un número negativo.")

            except(ValueError):

                print("\nEERROR: Tipo de dato invalido. Debe ser un número entero.")

        func.busqueda_precio(p_min , p_max , stock , productos)

    # == Actualizar precio == #

    elif (opc == 3):

        print("\n== ** Actualizar precio ** ==")

        while True:
            
            modelo = input("\nIngrese el nombre del modelo: ")

            while True:

                try:

                    p = int(input("\nIngrese precio nuevo: "))

                    if (p > 0):

                        break
                    
                    else:

                        print("\nERROR: El precio no puede ser un número negativo.")

                except(ValueError):

                    print("\nEERROR: Tipo de dato invalido. Debe ser un número entero.")

            if(func.actualizar_precio(modelo , p , stock)):

                print("\n¡Precio actualizado exitosamente!")

                print("\nAquí esta el stock actualizado con el nuevo precio: ")

                for modelo in stock:

                    print(f"\nModelo {modelo} : {stock[modelo]}")

            else:

                print("\nParece que el modelo no existe.")

            while True:

                valido = ["sí" , "si", "s" , "no", "n"]

                respuesta = input("\n¿Desea actualizar otro precio? (si/no): ").lower()

                if (respuesta in valido):

                    break

                else:

                    print("\nERROR: Respuesta invalida. Debe responder si o no.")

            if (respuesta == "no" or respuesta == "n"):

                break

    # == Salir de programa == #

    else:

        print("\nPrograma finalizado.")

        break