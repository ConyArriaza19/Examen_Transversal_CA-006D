# === LIBRERIA DE FUNCIONES === #

# === Función para ver stock por marca === #
def stock_marca(marca , productos , stock):

    stock_total = 0

    for producto in productos:

        if(productos[producto][0] == marca):

            for modelo in stock:

                if (modelo == producto):

                    stock_total += stock[modelo][1]

    print(f"\nLa cantidad de stock total de la marca {marca} es: {stock_total}")

# === Función para buscar por precios === #
def busqueda_precio(p_min , p_max , stock , productos):

    Modelos_seleccionados = []

    for modelo in stock:

        if (stock[modelo][0] >= p_min and stock[modelo][0] <= p_max and stock[modelo][1] != 0):

            for producto in productos:

                if (producto == modelo):

                    Marca = productos[producto][0]

                    Modelo = modelo

                    Formato =Marca + "--" + Modelo
            
                    Modelos_seleccionados.append(Formato)

    Modelos_seleccionados.sort()

    if (Modelos_seleccionados == []):
        
        print("\nNo hay notebooks en ese rango de precios.")

    else:

        print("\nLos notebooks entre los precios consultados son: ", Modelos_seleccionados)

# === Función para actualizar precios === #
def actualizar_precio(modelo , p , stock):

    actualizacion = 0
    
    for modelo_id in stock:

        if(modelo_id == modelo):

            stock[modelo_id][0] = p

            actualizacion += 1
            
    if (actualizacion == 0):

        return(False)        
        
    else:

        return(True)

