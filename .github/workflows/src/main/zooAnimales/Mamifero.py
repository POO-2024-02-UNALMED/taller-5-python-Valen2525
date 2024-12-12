from zooAnimales import Animal

class Mamifero(Animal):
    _cantidadMamiferos = 0
    def __init__(self, nombre, edad, habitat, genero, listado = [], caballos =None, leones =None, pelaje =None, patas =None):
        super(nombre, edad, habitat, genero)
        self._listado = listado.append(self)
        self.caballos = caballos
        self.leones =leones
        self._pelaje =pelaje
        self._patas =patas
        self._cantidadMamiferos += 1

    @classmethod
    def cantidadMamiferos(cls):
        return cls._cantidadMamiferos
    def crearCaballo(self, nombre, edad, genero):
        caballos +=1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        return caballo
    def crearLeon(self, nombre, edad, genero):
        leones +=1
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

