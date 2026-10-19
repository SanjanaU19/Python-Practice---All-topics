class Home:
    def __init__(self,address, color, rooms, floors, area, price):
        self.address = address
        self.color = color
        self.rooms = rooms
        self.floors = floors
        self.area = area
        self.price = price

h1 = Home("Katraj","White",4,5,"Narhe",200000)
h2 = Home("Bavdhan","Pink",5,2,"Bavdhan",600000)

print("this is object one")
print(h1.address)
print(h1.color)
print(h1.rooms)
print(h1.floors)
print(h1.area)
print(h1.price)

print("this is object two")
print(h2.address)
print(h2.color)
print(h2.rooms)
print(h2.floors)
print(h2.area)
print(h2.price)

