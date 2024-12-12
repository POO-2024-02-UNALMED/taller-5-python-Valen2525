class Animal():
    _totalAnimales = 0
    def __init__(self, nombre=None, edad =None, habitat=None, genero=None,zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        self._totalAnimales +=1

    def novimiento(self):
        return "desplazarse"
    @classmethod
    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.ave import Ave
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\n" + "Aves: " + Ave.cantidadAves() + "\n" + "Reptiles: " + Reptil.cantidadReptiles() + "\n" + "Peces: " + Pez.cantidadPeces() + "\n" +"Anfibios: " + Anfibio.cantidadAnfibios()
    def __str__(self):
        if self._zona ==None:
            return "Mi nombre es "+ self.getNombre()+", tengo una edad de " +self.getEdad()+ ", habito en "+self.getHabitat()+" y mi genero es "+self.getGenero()
        else:
            return "Mi nombre es "+ self.getNombre()+", tengo una edad de " +self.getEdad()+ ", habito en "+self.getHabitat()+" y mi genero es "+self.getGenero()+", la zona en la que me ubico es "+self.getZona().getNombre()+", en el "+ self.getZona().getZoo().getNombre()+"."
    def getNombre(self):
        return self._nombre
    def setNombre(self, nom):
        self._nombre = nom
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habi):
        self._habitat = habi
    def getGenero(self):
        return self._genero
    def setGenero(self, gen):
        self._genero = gen
    def getZona(self):
        return self._zona
    def setZona(self, zon):
        self._zona = zon
    def getTotalAnimales(self):
        return self._totalAnimales
    def setTotalAnimales(self, totAn):
        self._totalAnimales = totAn