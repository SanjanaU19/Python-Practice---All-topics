class Laptop:
    def __init__(self,pr,m,r,s,p):
        self.processor = pr
        self.model = m 
        self.ram = r 
        self.storage = s 
        self.price = p

l1 = Laptop("Intel","Dell","64GB","128 GB",50000)
l2 = Laptop("AMD", "HP", "16GB", "512 GB", 65000)

print(l1.processor)
print(l2.processor)

print(l1.model)
print(l2.price)