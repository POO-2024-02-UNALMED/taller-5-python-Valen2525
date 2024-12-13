from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorPlumas =None):
        super().__init__(nombre, edad, habitat, genero)
        Ave._listado.append(self)
        self._colorPlumas = colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    @classmethod
    def crearHalcon(self, nombre, edad, genero):
        Ave.halcones +=1
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        return halcon
    @classmethod
    def crearAguila(self, nombre, edad, genero):
        Ave.aguilas +=1
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        return aguila
    def novimiento(self):
        return "volar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colPlu):
        self._colorPlumas =colPlu