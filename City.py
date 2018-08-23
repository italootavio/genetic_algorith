import math
class City:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distanciaPara(self,cidade):
        distanciaX = abs(self.x - cidade.x)
        distanciaY = abs(self.y - cidade.y)
        return math.sqrt(math.pow(distanciaX,2)+math.pow(distanciaY,2))

    def __str__(self):
        return str(self.x)+" "+str(self.y)

class TourManager:
    def __init__(self):
        self.cidadesDeDestino = []

    def addCity(self,cidade):
        self.cidadesDeDestino.append(cidade)

    def getCidy(self,indice):
        return self.cidadesDeDestino[indice]

    def numberOfCities(self):
        return len(self.cidadesDeDestino)

class Tour:
    def __init__(self):
        self.tour = []
        self.fitness = 0
        self.distance = 0
teste = Tour
raise