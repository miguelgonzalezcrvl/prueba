vender = 0
venta_total = 0
entrada_Concepción = 500
entrada_Puente_Alto = 1300
entrada_Muelle_Barón_en_Valparaíso = 100
entrada_Muelle_Vergara_en_Viña_del_Mar = 50
Tipo_de_entrada_asignado = "G"
compra_entrada = {
    "entrada": []
}

def validad_texto(mensaje:str):
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("No debe tener espacio el nombre")
            continue
        return texto
    
def validad_numero_positivo(numero:int):
    while True:
        try:
            valor = int(input(numero))
            if valor <=0:
                print("El numero debe ser mayor a 0")
                continue
            return valor
        except ValueError:
            print("El numero no debe ser en decimal o escrito")

def validad_numero(numero:int):
    while True:
        valor = "1234567809"
        for i in numero:
            for n in valor:
                if i == n:
                    return True
        return False
    
def validad_letra(texto:str):
    while True:
        letra = "qwertyuiopñlkjhgfdsazxcvbnm"
        for i in texto:
            for n in letra:
                if i == n:
                    return True
        return False

def buscar_codigo(codigo:str):
    for i in compra_entrada["entrada"]:
        if i ["codigo"] == codigo:
            return i
    return None

def validad_mayuscula(mensaje:str):
    while True:
        letra = "QWERTYUIOPÑLKJHGFDSAZXCVBNM"
        for i in mensaje:
            for n in letra:
                if i == n:
                    return True
        return False

def validad_entrada(texto:str):
    while True:
        entrada = input(texto).lower()
        if entrada == "sun":
            return "sunset"
        elif entrada == "ni":
            return "night"
        else:
            print("Solo debe ingresar sun/ni")

while True:
    print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("[1]- Comprar entrada a “los Fortificados” en Concepción")
    print("[2]- Comprar entrada a “los Fortificados” en Puente Alto")
    print("[3]- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso")
    print("[4]- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar")
    print("[5]- Saliendo")

    opcion = validad_numero_positivo("Ingrese el numero donde desee ir: ")

    if opcion == 1:
        nombre = validad_texto("Ingrese el nombre del comprador: ")
        while True:
            codigo = input("Ingrese el codigo: ")
            if len(codigo) < 6:
                print("El caracteres debe tener al menos 6 digito")
                continue
            elif not validad_mayuscula(codigo):
                print("El codigo debe teber al menos una mayuscula")
                continue
            elif not validad_numero(codigo):
                print("El codigo debe tener al menos un numero")
            elif not validad_letra(codigo):
                print("El codigo debe tener una letra")
                continue
            break
        vender = int(input("Ingrese cuanto quiere comprar: "))
        venta_total = vender - entrada_Concepción

        agregar ={
            "nombre":nombre,
            "codigo":codigo,
            "venta_total":venta_total
        }
        compra_entrada["entrada"].append(agregar)
        print("la entrada se registra exitosamente")
        print(agregar)
    elif opcion == 2:
        nombre = validad_texto("Ingrese el nombre del ususario: ")
        while True:
            vender = int(input("Ingrese las entrada que debe comprar: "))
            if not vender < 4:
                print("Debe ingresar maximo 3 entrada")
                continue
            elif validad_numero_positivo(vender):
                venta_total = vender - entrada_Puente_Alto
                break
        agregar = {
            "nombre":nombre,
            "venta_total":venta_total
        }
        compra_entrada["entrada"].append(agregar)
        print("la entrada se registra exitosamente")
        print(agregar)
    elif opcion == 3:
        nombre = validad_texto("Ingrese el nombre: ")
        vender = int(input("Ingrese cuanto quiere comprar: "))
        venta_total = vender - entrada_Muelle_Barón_en_Valparaíso

        agregar= {
             "nombre":nombre,
             "Tipo de entrada asignado":Tipo_de_entrada_asignado,
             "venta_total": venta_total
        }
        compra_entrada["entrada"].append(agregar)
        print("la entrada se registra exitosamente")
        print(agregar)
    elif opcion == 4:
        nombre = validad_texto("Ingrese el nombre: ")
        tipo = validad_entrada("Ingrese la entrada sun/ni: ")
        vender = int(input("Ingrese cuanto quiere comprar: "))
        venta_total = vender - entrada_Muelle_Vergara_en_Viña_del_Mar

        agregar = {
            "nombre":nombre,
            "tipo":tipo,
            "venta_total":venta_total
        }
        compra_entrada["entrada"].append(agregar)
        print("la entrada se registra exitosamente")
        print(agregar)
    elif opcion == 5:
        print("Usted esta saliendo del programa")
        break
    else:
        print("Debe ingresar del 1 hasta el 6")
        break