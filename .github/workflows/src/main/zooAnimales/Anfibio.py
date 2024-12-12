from zooAnimales.Animal import Animal

class Anfibio(Animal):
    _cantidadAnfibios = 0
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, listado = [], colorPiel =None, venenoso =None):
        super().__init__(nombre, edad, habitat, genero)
        self._listado = listado.append(self)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._cantidadAnfibios += 1

    @classmethod
    def cantidadAnfibios(cls):
        return cls._cantidadAnfibios
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas +=1
        rana = Anfibio(nombre, edad, "pradera", genero, True, 4)
        return rana
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras +=1
        sala = Anfibio(nombre, edad, "selva", genero, True, 4)
        return sala
    def novimiento(self):
        return "saltar"
    def getListado(self):
        return self._listado
    def setListado(self, list):
        self._listado = list
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, colPi):
        self._colorPiel = colPi
    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self, ven):
        self._venenoso = ven