class Tree:
    def __init__(self, name, height, age, color, price):
        self.name = name
        self.height = height
        self.age = age
        self.color = color
        self.price = price

t1 = Tree("Mango", "10 feet", 5, "Green", 2000)

t2 = Tree("Apple", "5 feet", 10, "Red", 1000)

print(t1.name)
print(t2.name)

print(t1.age)
print(t2.age)

print(t1.height)
print(t2.height)