if __name__ == '__main__':
    import csv
    from clase import PlanAhorro
    listaPlanes = []
    archivo = open('planes.csv')
    reader = csv.reader(archivo, delimiter=(';'))
    for datos in reader:
        objeto = PlanAhorro(datos[0], datos[1],datos[2], datos[3])
        listaPlanes.append(objeto)
    '''for i in range(len(listaPlanes)):
        listaPlanes[i].mostrar() '''
    print("-----MENU DE OPCIONES----- \n 1_ ACTUALIZAR VALOR DEL VEHICULO\n 2_MOSTRAR PLANES INFERIORES A UN VALOR \n 3_ MONTO PARA LICITACION \n 4_MODIFICAR CANTIDAD DE CUOTAS PARA LICITACION")
    opcion = int(input())
    if(opcion == 1):
        for i in range(len(listaPlanes)):
             listaPlanes[i].mostrar()
             newValor = int(input("Ingrese el nuevo valor del vehiculo: "))
             listaPlanes[i].actualizacion(newValor)
    elif(opcion == 2):
        plata = float(input("Ingrese su monto a gastar: "))
        for i in range(len(listaPlanes)):
            if(listaPlanes[i].getValor() < plata):
                listaPlanes[i].mostrar()
    elif(opcion == 3):
        for i in range(len(listaPlanes)):
            print(f"Para el vehiculo: {listaPlanes[i].getCodigo()} se debe pagar un total de ${PlanAhorro.montoLicitacion(PlanAhorro.calcularCuota(listaPlanes[i].getValor()))} para su licitacion")
    elif(opcion == 4):
        cod = int(input("Ingrese el codigo del plan al que le quiere cambiar la cantidad de cuotas de licitacion: "))
        for i in range(len(listaPlanes)):
            if cod == listaPlanes[i].getCodigo():
                print("El plan es:")
                listaPlanes[i].mostrar()
                cant = int(input("Ingrese la nueva cantidad de cuotas para licitacion: "))
                listaPlanes[i].modificarCL(cant)
    else:
        print("Opcion invalida ")
    for i in range(len(listaPlanes)):
        listaPlanes[i].__str__()
     