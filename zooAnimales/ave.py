from zooAnimales.animal import Animal

class Ave(Animal):
    _cantidadAves = 0
    halcones = 0
    aguilas = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorPlumas =None):
        super().__init__(nombre, edad, habitat, genero)
        Ave._listado.append(self)
        self._colorPlumas = colorPlumas
        self._cantidadAves += 1

    @classmethod
    def cantidadAves(cls):
        return cls._cantidadAves
    @classmethod
    def crearHalcon(self, nombre, edad, genero):
        Ave.halcones +=1
        halcon = Ave(nombre, edad, "pradera", genero, True, 4)
        return halcon
    @classmethod
    def crearAguila(self, nombre, edad, genero):
        Ave.aguilas +=1
        aguila = Ave(nombre, edad, "selva", genero, True, 4)
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