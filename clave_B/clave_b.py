import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma():
    result = 2 + 4 + 6
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    x = 0
    suma = 0
    while x <= 1000:
        if x % 2 != 0:
            suma = suma + x
        x = x + 1
    return suma


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->
esferaDict = {"perimetro:", "area:", "volumen:"}


def definicionEsfera():
    return esferaDict


def obtenerPerimetro(radio):
    radio = 12
    perimetro = float(radio * 2 * math.pi)
    return perimetro
    esferaDict["perimetro"] = obtenerPerimetro()


def obtenerArea(radio):
    radio = 12
    area = float(4 * math.pi * radio ** 2)
    return area
    esferaDict["area"] = obtenerArea()


def obtenerVolumen(radio):
    radio = 12
    volumen = float((4 / 3) * math.pi * radio ** 3)
    return volumen
    esferaDict["volumen"] = obtenerVolumen()


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->

esferaDict = {"perimetro:", "area:", "volumen:"}


class Esfera:
    def __init__(self, radio=12):
        self.radio = radio

    def definicionEsfera(self):
        return esferaDict

    def obtenerPerimetro(self):
        perimetro = float(self.radio * 2 * math.pi)
        return perimetro
        esferaDict["perimetro"] = obtenerPerimetro()

    def obtenerArea(self):
        radio = 12
        area = float(4 * math.pi * self.radio ** 2)
        return area
        esferaDict["area"] = obtenerArea()

    def obtenerVolumen(self):
        radio = 12
        volumen = float((4 / 3) * math.pi * self.radio ** 3)
        return volumen
        esferaDict["volumen"] = obtenerVolumen()


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def procesar(self):
    banco.procesar(Cliente("balbino", "san salvador", 1, "abono", 250.0))
    banco.procesar(Cliente("rodrigo", "san salvador", 2, "retiro", 350.0))
    banco.procesar(Cliente("marta", "san salvador", 3, "abono", 400.0))
    banco.procesar(Cliente("rafael", "santa ana", 4, "abono", 500.0))
    banco.procesar(Cliente("balbino", "la libertad", 1, "abono", 250.0))
    banco.procesar(Cliente("marta", "san salvador", 3, "abono", 250.0))
    banco.procesar(Cliente("rodrigo", "san salvador", 2, "abono", 100.0))
    
    def abonosSanSalvador(self):
        for x in Banco
         totalAbonos=sum(Cliente[2])
           if (Cliente[1]=="san salvador")

        return totalAbonos

    def abonosBalYRod(self):
        return 0


class Cliente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
