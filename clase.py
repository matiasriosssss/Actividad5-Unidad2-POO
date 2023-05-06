class PlanAhorro:
    __cantCuotas = 60
    __cuotasLicitacion = 10
    def __init__(self, codigo, modelo, version, valor):
        self.__codigo = int(codigo)
        self.__modelo = modelo
        self.__version = version
        self.__valor = float(valor)
    def __str__(self):
        print(f"Codigo de plan: {self.__codigo}, Modelo: {self.__modelo}, Version: {self.__version}, Valor: {self.__valor}, Cuotas: {self.__cantCuotas}, Cuotas Licitacion: {self.__cuotasLicitacion} ")
    def mostrar(self):
        print(f"Codigo de plan: {self.__codigo}, Modelo: {self.__modelo}, Version: {self.__version} ")
    def actualizacion(self, nuevoValor):
        self.__valor = nuevoValor
        print("Valor actualizado ")
    def getValor(self):
        return self.__valor
    def getCodigo(self):
        return self.__codigo
    def modificarCL(self, cantidad):
        self.__cuotasLicitacion = cantidad
        print("Cantidad de cuotas para licitacion modificada con exito ")
    @classmethod
    def calcularCuota(cls, valorAuto):
        valorCuota = ((valorAuto / cls.__cantCuotas) * 0.10)   
        return valorCuota
    @classmethod
    def montoLicitacion(cls, precioCuota):
        monto = precioCuota * cls.__cuotasLicitacion
        return monto
