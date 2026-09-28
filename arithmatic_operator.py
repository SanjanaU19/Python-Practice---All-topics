a = 12
b = 10
# Arithmatic Operators 
print("Addition of a + b =",a + b)
print("Substraction of a - b =",a - b)
print("Multiplication of a * b =",a * b)
print("Division of a / b =",a / b)   # it return the float value 
print("Floor division of a // b = ",a //b)  # it return the int value
print("Modulus of a % b :" , a % b) # return the reminder
print("Power of a ** b = ", a ** b)

# str & int 
s1 = "abc"
s2 = 10
s3 = 5.5
# print(s1 + s2 ) # TypeError: can only concatenate str (not "int") to str
# print(s1 + s3)  # TypeError: can only concatenate str (not "float") to str
print(s1 * s2) # abcabcabcabcabcabcabcabcabcabc

s4 = "abc"
s5 = "10"
print(s4 + s5) # abc10

# float & Int
b1 = 10.3
b2 = 12
print(b1 + b2)  # 22.3
print(b1-b2)
print(b1 * b2)
print(b1 / b2)
print(b1 // b2)
print(b1 % b2)
print(b1 ** b2)

# boolean & boolean  -> Return a int value
print(True + True)  # 2
print(False + False)  # 0
print(True + False)   # 1
print(False + True)   # 1

# complex & complex
d1 = 1 + 2j
d2 = 5 + 7j

print(d1 + d2)
print(d1 - d2)
print(d1 * d2)
print(d1 / d2)
# print(d1 // d2) # unsupported operand type(s) for //: 'complex' and 'complex'
# print(d1 % d2) --> unsupported operand type(s) for %: 'complex' and 'complex'

# str - str
e1 = "Insta"
e2 = "gram"
print(e1 + e2)
# print(e1 - e2) ->  unsupported operand type(s) for -: 'str' and 'str'
# print(e1 * e2) ->  can't multiply sequence by non-int of type 'str'
# print(e1 / e2) -> # unsupported operand type(s) for /: 'str' and 'str'
# print(e1 // e2) -> # unsupported operand type(s) for /: 'str' and 'str'
# print(e1 % e2)  -> TypeError: not all arguments converted during string formatting 


n1 = 123
n2 = 10
# 3 12
r1 = n1 % n2
q1 = n1 // n2
print(r1 , q1)

# 2 1
r2 = q1 % 10
q2 = q1 // 10
print(r2 , q2)

# 1 0 
r3 = q2 % 10
q3 = q2 // 10
print(r3 ,q3)

print("Sum of n1 : ", r1 + r2 + r3)
print("Mul of n1 : ", r1 * r2 * r3)