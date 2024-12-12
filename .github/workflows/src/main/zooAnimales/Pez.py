from zooAnimales.Animal import Animal

class Pez(Animal):
    _cantidadPeces = 0
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, listado = [], colorEscamas =None, cantAletas =None):
        super().__init__(nombre, edad, habitat, genero)
        self._listado = listado.append(self)
        self._colorEscamas = colorEscamas
        self._cantidadAletas =cantAletas
        self._cantidadPeces += 1

    @classmethod
    def cantidadPeces(cls):
        return cls._cantidadPeces
    @classmethod
    def crearSalmon(self, nombre, edad, genero):
        self.salmones +=1
        salmon = Pez(nombre, edad, "pradera", genero, True, 4)
        return salmon
    @classmethod
    def crearBacalao(self, nombre, edad, genero):
        self.bacalaos +=1
        bacalao = Pez(nombre, edad, "selva", genero, True, 4)
        return bacalao
    def novimiento(self):
        return "nadar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colEs):
        self._colorEscamas =colEs
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantAletas):
        self._cantidadAletas = cantAletas