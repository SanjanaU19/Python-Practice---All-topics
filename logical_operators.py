# and operator
a = True
b =  False
m = a and b
print(m)  # False

c = False
d = True
e = c and d
print(e) # false

f = False
g = False
i = f and g 
print(i)  # false 

j = True
k = True
l = j and k
print(l) # true

#  or operators
s1 = True
s2 = False
print(s1 or s2)

s3 = False
s4 = True
print(s3 or s4)

s5 = True
s6 = True
print(s5 or s6)

s7 = False
s8 =  False
print(s7 or s8)

# not operator

print(not True) # False
print(not False) # True

print(not (True and True)) # F
print(not (True or False)) # F
print(not (False or False)) # T

username = "abc@1234"
password = "xyz1234"

if username == "abc@1234" and password == "xyz1234":
    print("Welcome To The Login Page.....")
else:
    print("Invalid Username and password....")