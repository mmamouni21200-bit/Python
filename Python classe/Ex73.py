"""Classes:
Crear una classe anomenada Animal que tingui els següents atributs d’objecte: especie i edat i els següents mètodes: xerrar (abstracte), mourem (abstracte) i quisoc. Llavors, crearem diferents subclasses:  Cavall, Dofí, Abella, Humà, Centaure.... que hauran de redefinir aquestes mètodes. Crearem una nova subclasse d’Humà, anomenada Fiet. Llavors, crearem una subclasse Centaure que heredarà de Cavall i Humà. Finalment, tindrem una nova classe xou que no té cap relació amb els altres, però que té els mateixos mètodes que Animal implementats.
Abella crearà un nou mètode anomenat, picar.
Humà tindrà un nou atribut d’objecte anomenat, nom.
Fiet tindrà un nou atribut d’objecte anomenat, pares (llista). I un nou mètode anomenat nompares que ens mostrarà el nom dels pares.
Amb això, crear un llista d’elements de cada tipus i un for (bucle) que cridi als mètodes iguals.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return "Sóc un {} de {} anys.".format(self.especie, self.edat)
class Cavall(Animal):
    def xerrar(self):
        return "Neigh!"

    def mourem(self):
        return "El cavall galopa."
class Dofi(Animal):
    def xerrar(self):
        return "Click-click!"

    def mourem(self):
        return "El dofí nedar."
class Abella(Animal):
    def xerrar(self):
        return "Bzzzz!"

    def mourem(self):
        return "L'abella vola."

    def picar(self):
        return "L'abella pica!"
class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        return "Hola!"

    def mourem(self):
        return "L'humà camina." 