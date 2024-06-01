import time
import os


print('Bienvenido a la app registro de clientes!')
time.sleep(1)
os.system('cls')


lista_ruts = []
lista_digits_verf = []
lista_nombres = []
lista_apellidos = []
lista_direcciones = []
lista_telefono = []

while True:
    os.system('cls')
    print('Menú registro clientes\n\t 1. Agregar un cliente\n\t 2. Buscar cliente\n\t 3. Eliminar cliente\n\t 4. Salir')
    while True:
        try:
            opc = int(input('Ingrese una opción: '))
            if opc in (1, 2, 3, 4):
                break
            else:
                print(
                    'ERROR! debe ingresar una opción valida, opciones valida(1,2,3,4)!')
        except:
            print('ERROR! debe ingresar números enteros!')

    if opc == 1:
        print('Agregar cliente!')
        time.sleep(1)
        os.system('cls')
        while True:
            try:
                rut = int(
                    input('Ingrese su rut(sin puntos y sin codigo verificador): '))
                if rut >= 4000000 and rut <= 99999999:
                    print('Rut registrado exitosamente!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! debe ingresar un rut valido, el rut debe estar dentro del rango 4000000 a 99999999!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar números enteros!')

        if rut in lista_ruts:
            print('ESTE RUT YA SE ENCUENTRA REGISTRADO!')
            time.sleep(1)
            continue

        while True:
            digito_verf = str(
                input('Ingrese su digito verificador de su rut: '))
            if digito_verf in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "K"):
                print('Digito de verificación registrado exitosamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! debe ingresar un digito de verificación valido, digitos validos("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "K")!')
            time.sleep(1)
            os.system('cls')

        while True:
            nombre = str(input('Ingrese su nombre: '))
            if len(nombre.strip()) >= 3:
                print('Nombre registrado exitosamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! el nombre debe contener al menos 3 letras!')

        while True:
            apellido = str(input('Ingrese su apellido: '))
            if len(apellido.strip()) >= 3:
                print('Apellido registrado exitosamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! el apellido debe contener al menos 3 letras!')

        while True:
            direccion = str(input('Ingrese su dirección: '))
            if len(direccion.strip()) >= 7:
                print('Direccion registrada exitosamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! la dirección debe contener al menos 7 letras!')

        while True:
            try:
                telefono = int(input('Ingrese su número celular(9 digitos): '))
                if len(str(telefono)) == 9:
                    print('Numero de celular registrado exitosamente!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print('ERROR! debe ingresar 9 digitos!')
            except:
                print('ERROR! debe ingresar números enteros!')

        lista_ruts.append(rut)
        lista_digits_verf.append(digito_verf)
        lista_nombres.append(nombre)
        lista_apellidos.append(apellido)
        lista_direcciones.append(direccion)
        lista_telefono.append(telefono)

    elif opc == 2:
        print('Buscar cliente!')
        time.sleep(1)
        os.system('cls')

        if len(lista_ruts) >= 1:
            while True:
                try:
                    rut_buscar = int(
                        input('Ingrese el rut que desea buscar(sin puntos y sin digito verificador): '))
                    if rut_buscar in lista_ruts:
                        posicion = lista_ruts.index(rut_buscar)
                        print('Cliente encontrado!')
                        print(f"""                                Rut:{lista_ruts[posicion]}
                              Digito verificador:{lista_digits_verf[posicion]}\t
                              Nombre:{lista_nombres[posicion]}\t
                              Apellido:{lista_apellidos[posicion]}\t
                              Direccion:{lista_direcciones[posicion]}\t
                              Telefono:{lista_telefono[posicion]}
                            """)
                        mensaje = int(input(
                            'Deseas salir? (Ingrese 1: salir) (Ingrese 0: redigir a buscar cliente): '))
                        if mensaje == 1:
                            print('Saliendo.')
                            time.sleep(1)
                            os.system('cls')
                            break
                        else:
                            print('Redirigiendo.')
                        time.sleep(1)
                        os.system('cls')
                    else:
                        print(
                            'NO HAY NINGUN CLIENTE REGISTRADO CON EL RUT INGRESADO!')
                except:
                    print('ERROR! debe ingresar números enteros!')
        else:
            print('NO CLIENTES REGISTRADOS!')
            time.sleep(1)

    elif opc == 3:
        if len(lista_ruts) >= 1:
            print('Eliminar cliente!')
            time.sleep(1)
            os.system('cls')

            for i in range(len(lista_ruts)):
                print("LISTA DE CLIENTES REGISTRADOS\n")
                print(
                    'RUT:', lista_ruts[i], "\tDigito Verificador:", lista_digits_verf[i], "\tNombre:", lista_nombres[i], "\tApellido:", lista_apellidos[i], "\tDirección:", lista_direcciones[i], "\tTelefono:", lista_telefono[i])

            while True:
                if len(lista_ruts) >= 1:
                    rut_eliminar = int(input('Ingrese un rut a eliminar: '))
                    mensaje = int(
                        input('(Ingrese 0: para eliminar) (Ingrese 1: no eliminar y salir): '))
                    if mensaje == 1:
                        print('Saliendo.')
                        break
                    else:
                        if mensaje == 0:
                            posicion = lista_ruts.index(rut_eliminar)
                            if rut_eliminar in lista_ruts:
                                lista_ruts.pop(posicion)
                                lista_digits_verf.pop(posicion)
                                lista_nombres.pop(posicion)
                                lista_apellidos.pop(posicion)
                                lista_direcciones.pop(posicion)
                                lista_telefono.pop(posicion)
                                print('CLIENTE ELIMINADO!')
                                time.sleep(1)
                                os.system('cls')
                            else:
                                print(
                                    'El rut ingresado no se encuentra registrado!')
                else:
                    print('NO HAY CLIENTES PARA ELIMINAR')
                    time.sleep(1)
                    os.system('cls')
                    print('Saliendo de eliminar clientes!')
                    time.sleep(1)
                    break
        else:
            print('NO HAY CLIENTES INGRESADOS!')
            time.sleep(1)

    else:
        for x in range(1, 4):
            print('Saliendo de app registro de clientes', ("."*x))
            time.sleep(1)
            os.system('cls')
        break
