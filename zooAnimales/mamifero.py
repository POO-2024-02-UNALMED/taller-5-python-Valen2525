from zooAnimales.animal import Animal

class Mamifero(Animal):
    _cantidadMamiferos = 0
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje =None, patas =None):
        super().__init__(nombre, edad, habitat, genero)
        Mamifero._listado.append(self)
        self._pelaje =pelaje
        self._patas =patas
        self._cantidadMamiferos += 1

    @classmethod
    def cantidadMamiferos(cls):
        return cls._cantidadMamiferos
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos +=1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return caballo
    @classmethod
    def crearLeon(self, nombre, edad, genero):
        Mamifero.leones +=1
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        return leon

    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getPelaje(self):
        return self._pelaje
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPatas(self):
        return self._patas
    def setPatas(self, patas):
        self._patas = patas
