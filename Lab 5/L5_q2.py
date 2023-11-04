class Vehicle:
    def __init__(self, owner, id, manufacturer):
        self.owner = owner
        self.id = int(id)
        self.manufacturer = manufacturer

class Passenger(Vehicle):
    def __init__(self, owner, id, manufacturer, capacity):
        super().__init__(owner, id, manufacturer)
        self.capacity = int(capacity)

    def displayDetails(self):
        print("Owner name: ", self.owner)
        print("Vehicle ID: ", self.id)
        print("Manufacturer Name: ", self.manufacturer)
        print("Number of Passengers: ", self.capacity)

n = int(input("Enter the number of Vehicles: "))
passengers = []

for i in range(n):
    owner = input("Enter owner name: ")
    id = input("Enter vehicle id: ")
    manufacturer = input("Enter manufacturer: ")
    capacity = int(input("Enter capacity: "))
    passenger = Passenger(owner, id, manufacturer, capacity)
    passengers.append(passenger)

for passenger in passengers:
    passenger.displayDetails()
