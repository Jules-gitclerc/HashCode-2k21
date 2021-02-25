class Configuration:
    emulatorDuration = -1
    intersectionNumber = -1
    streetNumber = - 1
    carsNumber = -1
    bonusPoint = -1
    streetSet = set()
    carsList = []
    intersectionList = []

    def addEndIntersection (self, street):
        hasFound = False
        for item in self.intersectionList:
            if item.id == street.endIntersectionId and hasFound == False:
            item.streetOut.append(street)
            hasFound = True
            if hasFound == False:
                inter = Intersection()
                inter.id = street.endIntersectionId
                inter.streetOut = [street]
                inter.streetIn = []
                self.intersectionList.append(inter)

    def __str__ (self):
        return f"emulation for {self.emulatorDuration} seconds\n{self.intersectionsNumber} streets\n{self.carsNumber} cars\n{self.bonusPoint}"

class Street:
    startIntersectionId = -1
    endIntersectionId = -1
    streetName = ""
    streetTravelDuration = -1

    def __str__ (self):
        return f"start : {self.startIntersectionId} end : {self.endIntersectionId} name : {self.streetName} duration : {self.streetTravelDuration}"

class Car:
    id = -1
    streetsIn = list()
    streetsOut = list()

    def __str__ (self):
        return f"street to travel : {self.streetToTravelNumber} travel to do : {self.streetToTraveSet}"

class Intersection:
    id = -1
    streetIn = list()
    streetOut = list()

    def __str__ (self):
        return f"id : {self.id} streetIn : {self.streetIn} streetOut : {self.streetOut}"

class IntersectionSchedule:
    intersection = None
    streetsSchedule = { }

    def addStreet(self, name, duration):
        self.streetsSchedule[name] = duration

currentConfig = Configuration()

def read_line(fileDescriptor):
    return fileDescriptor.readLine().replace("\n", "")

def read_files(filename = "a.txt"):
    f = open(filename, " r ")
    intArray = list(map(lambda x: int(x), read_line(f).split(" ")))
    currentConfig.emulatorDuration = intArray[0]
    currentConfig.intersectionNumber = intArray[1]
    currentConfig.streetsNumber = intArray[2]
    currentConfig.streetNumber = intArray[3]
    currentConfig.bonusPoint = intArray[4]

def doOutput(filename, schedule):
    f = open(filename, 'w')
    f.write(len(schedule))
    for item in schedule:


def compute():
    for car in currentConfig.carsList:
        for street in car.streetToTravelSet:
            currentConfig.streetSet[street].weightCars += 1

    schedule = []
    for i in range(len(currentConfig.intersectionList)):
        intersection = currentConfig.intersectionList[i]
        intersectionSchedule = IntersectionSchedule()
        intersectionSchedule.streetSSchedule = []
        intersectionSchedule.intersection = intersection
        for street in intersection.streetOut:
            if 
                intersectionSchedule.addStreet(street.streetName, 1)
        schedule.append(intersectionSchedule)
    return schedule

if __name__ == '__main__':
    read_files("a_example.txt")
    schedule = compute()
    doOutput("a.out", schedule)
