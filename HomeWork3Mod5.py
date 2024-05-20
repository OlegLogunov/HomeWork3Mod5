class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if (self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType):
            return True


numberOfFloors = 0
buildingType = None

MyHome = Building(24, "Кирпичный")

print("Этажность Вашего дома:")
YourNumberOfFloors = int(input(numberOfFloors))
print("Тип Вашего дома:")
YourBuildingType = input(str(buildingType))
YourHome = Building(YourNumberOfFloors, YourBuildingType)

if MyHome == YourHome:
    print("Дома очень похожи")
else:
    print("Абсолютно разные дома")
