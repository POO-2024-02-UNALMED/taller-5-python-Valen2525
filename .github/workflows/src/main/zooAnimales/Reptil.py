from zooAnimales import Animal

class Reptil(Animal):
    _cantidadReptiles = 0
    def __init__(self, nombre, edad, habitat, genero, listado = [], iguanas =None, serpientes =None, colorEscamas =None, largoCola =None):
        super(nombre, edad, habitat, genero)
        self._listado = listado.append(self)
        self.iguanas = iguanas
        self.serpientes = serpientes
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._cantidadReptiles += 1
    
    @classmethod
    def cantidadReptiles(cls):
        return cls._cantidadReptiles
    def crearIguana(self, nombre, edad, genero):
        iguanas +=1
        iguana = Reptil(nombre, edad, "pradera", genero, True, 4)
        return iguana
    def crearSerpiente(self, nombre, edad, genero):
        serpientes +=1
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