import math
import matplotlib.pyplot as plt
from random import shuffle
from random import randint
from Maps import *

class City:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def randCity(self):
        self.x = randint(0,500)
        self.y = randint(0,500)

    def distanceTo(self,cidade):
        distanciaX = abs(self.x - cidade.x)
        distanciaY = abs(self.y - cidade.y)
        return math.sqrt(math.pow(distanciaX,2)+math.pow(distanciaY,2))

    def __str__(self):
        return str(self.x)+","+str(self.y)

    def __repr__(self):
        return "("+str(self.x) + "," + str(self.y)+")"
class TourManager:
    destinationCities = []

    @staticmethod
    def addCity(cidade):
        TourManager.destinationCities.append(cidade)

    @staticmethod
    def getCidy(indice):
        return TourManager.destinationCities[indice]

    @staticmethod
    def numberOfCities():
        return len(TourManager.destinationCities)


class Tour:
    def __init__(self):
        self.tour = []
        self.fitness = 0
        self.distance = 0
        for i in range(0,TourManager.numberOfCities()):
            self.tour.append(None)

    def generateIndividual(self):
        for i in range(0,TourManager.numberOfCities()):
            self.setCity(i,TourManager.getCidy(i))
        shuffle(self.tour)

    def getCity(self,tourPosition):
        return self.tour[tourPosition]

    def setCity(self,tourPosition,city):
        self.tour[tourPosition] = city
        self.fitness = 0
        self.distance = 0

    def getFitness(self):
        if self.fitness is 0:
            self.fitness = 1/float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for i in range(0,self.tourSize()):
                fromCity = self.getCity(i)
                destinationCity = City(0,0)
                destinationCity.randCity()
                if i+1 < self.tourSize():
                    destinationCity = self.getCity(i+1)
                else:
                    destinationCity = self.getCity(0)
                tourDistance+=fromCity.distanceTo(destinationCity)

            self.distance = tourDistance
        return int(self.distance)

    def tourSize(self):
        return len(self.tour)

    def containsCity(self,city):
        if city in self.tour:
            return True
        return False

    def __str__(self):
        gene = "|"
        for i in range(0,self.tourSize()):
            gene+=str(self.getCity(i))+"|"
        return gene
    def __repr__(self):
        gene = "|"
        for i in range(0, self.tourSize()):
            gene += str(self.getCity(i)) + "|"
        return gene

class Population:
    def __init__(self,populationSize,initialise):
        self.tours = []
        for i in range(0,populationSize):
            self.tours.append(None)
        if initialise:
            for i in range(0,self.populationSize()):
                newTour = Tour()
                newTour.generateIndividual()
                self.saveTour(i,newTour)

    def saveTour(self,index, tour):
        self.tours[index] = tour

    def getTour(self,index):
        return self.tours[index]

    def getFittest(self):
        fittest = self.tours[0]
        for i in range(1,self.populationSize()):
            if fittest.getFitness() <= self.getTour(i).getFitness():
                fittest = self.getTour(i)
        return fittest

    def populationSize(self):
        return len(self.tours)


class GA:
    mutationRate = 15 # 0.015
    tournamentSize = 5
    elitism = True

    @staticmethod
    def evolvePopulation(pop):
        newPopulation = Population(pop.populationSize(),False)
        elitismOffset = 0
        if GA.elitism:
            newPopulation.saveTour(0,pop.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = GA.tounamentSelection(pop)
            parent2 = GA.tounamentSelection(pop)
            child = GA.crossover(parent1,parent2)
            newPopulation.saveTour(i,child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            GA.mutate(newPopulation.getTour(i))

        return newPopulation

    @staticmethod
    def crossover(parent1, parent2):
        child = Tour()

        starPos = randint(0, parent1.tourSize())
        endPos = randint(0, parent1.tourSize())

        for i in range(0, child.tourSize()):
            if starPos < endPos and i > starPos and i < endPos:
                child.setCity(i, parent1.getCity(i))
            elif starPos > endPos:
                if not (i < starPos and i > endPos):
                    child.setCity(i, parent1.getCity(i))

        for i in range(0, parent2.tourSize()):
            if not child.containsCity(parent2.getCity(i)):
                for ii in range(0, child.tourSize()):
                    if child.getCity(ii) is None:
                        child.setCity(ii, parent2.getCity(i))
                        break

        return child

    @staticmethod
    def mutate(tour):
        for tourPos1 in range(0,tour.tourSize()):
            if randint(0,100) < GA.mutationRate:
                tourPos2 = randint(0,tour.tourSize()-1)

                city1 = tour.getCity(tourPos1)
                city2 = tour.getCity(tourPos2)

                tour.setCity(tourPos2,city1)
                tour.setCity(tourPos1, city2)


    @staticmethod
    def tounamentSelection(pop):
        tournament = Population(GA.tournamentSize,False)
        for i in range(0,GA.tournamentSize):
            randomId = randint(0,pop.populationSize()-1)
            tournament.saveTour(i,pop.getTour(randomId))
        fittest = tournament.getFittest()
        return fittest
class TSP_GA:
    def __init__(self):

        city = City(60,200)
        TourManager.addCity(city)
        city = City(180, 200)
        TourManager.addCity(city)
        city = City(80, 180)
        TourManager.addCity(city)
        city = City(140, 180)
        TourManager.addCity(city)
        city = City(20, 160)
        TourManager.addCity(city)
        city = City(100, 160)
        TourManager.addCity(city)
        city = City(200, 160)
        TourManager.addCity(city)
        city = City(140, 140)
        TourManager.addCity(city)
        city = City(40, 120)
        TourManager.addCity(city)
        city = City(100, 120)
        TourManager.addCity(city)
        city = City(180, 100)
        TourManager.addCity(city)
        city = City(60, 80)
        TourManager.addCity(city)
        city = City(120, 80)
        TourManager.addCity(city)
        city = City(180, 60)
        TourManager.addCity(city)
        city = City(20, 40)
        TourManager.addCity(city)
        city = City(100, 40)
        TourManager.addCity(city)
        city = City(200, 40)
        TourManager.addCity(city)
        city = City(20, 20)
        TourManager.addCity(city)
        city = City(60, 20)
        TourManager.addCity(city)
        city = City(160, 20)
        TourManager.addCity(city)
        '''
        for i in range(0,25):
            city = City(0,0)
            city.randCity()
            TourManager.addCity(city)
        '''
        pontosX = []
        pontosY = []

        for i in range(0,TourManager.numberOfCities()):
            pontosX.append(TourManager.getCidy(i).x)
            pontosY.append(TourManager.getCidy(i).y)
        plt.plot(pontosX,pontosY,"ro")

        plt.show()

        pop = Population(50,True)
        print("Distância inicial: "+str(pop.getFittest().getDistance()))

        pop = GA.evolvePopulation(pop)
        for i in range(0,500):
            pop = GA.evolvePopulation(pop)

        print("Finalizado")
        print("Distância Final: "+str(pop.getFittest().getDistance()))
        print("Solução: ")
        print(pop.getFittest())
        print(pop.getFittest().tour)
        plt.plot(pontosX, pontosY, "ro")
        pontosX = []
        pontosY = []
        for i in pop.getFittest().tour:
            pontosX.append(i.x)
            pontosY.append(i.y)
        plt.plot(pontosX, pontosY)
        plt.show()


ma = TSP_GA()