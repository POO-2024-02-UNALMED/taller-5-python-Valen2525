from zooAnimales.animal import Animal

class Reptil(Animal):
    _cantidadReptiles = 0
    iguanas = 0
    serpientes = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorEscamas =None, largoCola =None):
        super().__init__(nombre, edad, habitat, genero)
        Reptil._listado.append(self)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._cantidadReptiles += 1
    
    @classmethod
    def cantidadReptiles(cls):
        return cls._cantidadReptiles
    @classmethod
    def crearIguana(self, nombre, edad, genero):
        Reptil.iguanas +=1
        iguana = Reptil(nombre, edad, "pradera", genero, True, 4)
        return iguana
    @classmethod
    def crearSerpiente(self, nombre, edad, genero):
        Reptil.serpientes +=1
        serp = Reptil(nombre, edad, "selva", genero, True, 4)
        return serp
    def novimiento(self):
        return "resptar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colEs):
        self._colorEscamas =colEs
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self, larCol):
        self._largoCola =larCol