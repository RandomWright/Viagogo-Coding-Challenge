# Charlotte Wright
# Python 2.7

import random
import uuid

events = []
idnum = 0


class Event(object):

    def __init__(self, price, loc):
        self.identifier = createID()
        self.prices = price
        self.loc = loc
        self.dist = 0

    def getDist(self, person):
        if len(self.prices) == 0: #This event is full
            return -1
        self.dist = abs(self.loc[0] - person[0]) + abs(self.loc[1] - person[1])
        return self.dist #Manhattan Distance
        

    def getPrice(self):
        if len(self.prices) == 0: #No tickets left
            return -1
        else:
            self.prices.sort()
            return '${0:.2f}'.format(self.prices[0])

    def __str__(self):
        return "Event " + str(self.identifier) + " - " + str(self.getPrice()) + ", Distance " + str(self.dist)

def createID(): #Create Unique identifier
    global idnum
    idnum = idnum + 1
    return idnum

def generateSeed():
    one = random.randint(-10, 10)
    two = random.randint(-10, 10)
    return [one, two]

def addEvent(prices):
    loc = generateSeed()
    event = Event(prices, loc)
    events.append(event)
    return idnum + 1

def sampleEvents():
    addEvent([12.00, 13.00, 20.00, 3.04])
    addEvent([3.00, 4.05, 12.10])
    addEvent([])
    addEvent([100.00, 1220.00, 30.00])
    addEvent([3.00, 23.00, 2.00])
    addEvent([10.00, 10.00, 100.50])
    addEvent([50.00])
    addEvent([10.00])

def findClosest(person):
    distance = {}
    for e in events:
        dist = e.getDist(person)
        if dist != -1:
            distance[dist] = e

    listOf = distance.keys()
    listOf.sort()
    for x in range(0, 5):
        if x > len(listOf):
            break
        person = listOf[x]
        print distance[person]

def main():
    sampleEvents()
    x = input("Please Input Coordinates \n")
    findClosest(x)

if  __name__ =='__main__':main()
