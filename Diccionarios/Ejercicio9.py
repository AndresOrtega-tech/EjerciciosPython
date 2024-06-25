# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
# el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el 
# número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad 
# pendiente de cobro.


facturas = {}
bandera = 'si'

cantidadPagada = 0
cantidadPendiente = 0


while bandera == 'si':

    if len(facturas) > 0:
        menu = input('''
        - Si desea anadir una factura escriba A
        - Si desea pagar una factura escriba P
        - Si desea terminar una factura escriba T
        Desicion: ''')
    else:
        menu = input('''
        - Si desea anadir una factura escriba A
        - Si desea salir de la operacion escriba N
        Desicion: ''')

        if menu == 'N': bandera = 'no'
    
    
    
    if menu == 'A':
        clave = input('Escribe el numero de facutra: ')
        valor = int(input('Escribe el precio de factura: '))
        facturas[clave] = valor
        cantidadPendiente += valor
        
        bandera = input('Desea continuar si/no: ')

    elif menu == 'T':
        numeroFactura = input('Cual es el numero de factura: ')
        if numeroFactura in facturas:
            cantidadPagada += facturas[numeroFactura]
            cantidadPendiente -= facturas[numeroFactura]
            facturas.pop(numeroFactura)
        else: print('No esta disponible la factura')

        bandera = input('Desea continuar si/no: ')
    
    elif menu == 'P':
        numeroFactura = input('Cual es el numero de factura: ')
        if numeroFactura in facturas:
            cantidadPagar = int(input(f'Escribe la cantidad que vas a pagar, esta pendiende {facturas[numeroFactura]}: '))
            cantidadPagada += cantidadPagar
            cantidadPendiente -= cantidadPagar
            facturas[numeroFactura] = facturas[numeroFactura]-cantidadPagar
        else: print('No esta disponible la factura')

        bandera = input('Desea continuar si/no: ')
    
    print(facturas)
    print(f'Cantidad pagada : {cantidadPagada}')
    print(f'Cantidad pendiente: {cantidadPendiente}')