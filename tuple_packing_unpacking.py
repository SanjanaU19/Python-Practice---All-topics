p1 = "Tshirt"
p2 ="Jeans"
p3 = "Jacket"
p4 = "Charger"
p5 = "Cash"

# list and tuple
bag1 = [p1,p2,p3,p4,p5]
bag2 = (p1,p2,p3,p4,p5)

print("bag1: ",bag1)
print("Bag2:",bag2)

# List and tuple supports unpacking the elements
e1,e2,e3,e4,e5 = bag2
print("e1:",e1)
print("e2:",e2)
print("e3:",e3)
print("e4:",e4)
print("e5:",e5)

# imp -> 
e1 , e2 , *e3 = bag2
print("e1:",e1)
print("e2:",e2)
print("e3:",e3) 
# output of above code
# e1: Tshirt
# e2: Jeans
# e3: ['Jacket', 'Charger', 'Cash']