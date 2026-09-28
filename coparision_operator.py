# int - int
s1 = 22
s2 = 23
print(s1 > s2) # false
print(s1 < s2) # true
print(s1 == s2) # false
print(s1 != s2) # true
print(s1 <= s2) # true
print(s1 >= s2) # false

# str - str  -> String comparison is based on Unicode/lexicographical order, not string length alone.
a1 = "apple"
a2 = "banana"
print(a1 > a2) # f
print(a1 < a2)  # T
print(a1 == a2)  # F
print(a1 != a2)  # T
print(a1 <= a2) # T
print(a1 >= a2)  # F

# float - float 
f1 = 5.6
f2 = 1.9
print(f1 < f2) # F
print(f1 > f2) # T
print(f1 == f2) # F
print(f1 != f2)  # T
print(f1 >= f2)  # T
print(f1 <= f2)  # F

# bool - bool  -> it compare based on True = 1 and False = 0 format
b1 = True
b2 = False
print(b1 > b2) #True
print(True > False)   # True
print(False > True)   # False
print(True == 1)      # True
print(False == 0)     # True
print(True < False)   # False
print(True >= False)  # True
print(False <= True)  # True

# str - int
i1 = "abc"
i2 = 10
print(i1 == i2)  # False
print(i1 != i2)  # True
# print(i1 < i2) ->  '<' not supported between instances of 'str' and 'int'
# print(i1 > i2) ->  '<' not supported between instances of 'str' and 'int'
# print(i1 >= i2) ->  '>=' not supported between instances of 'str' and 'int'
# print(i1 <= i2) --> '<=' not supported between instances of 'str' and 'int'

# bool - int
t1 = True  # 1
t2 = 10
print(t1 > t2) # F
print(t1 < t2) # T
print(t1 == t2) #F
print(t1 != t2) # T 
print(t1 >= t2) # F
print(t1 <= t2) # T

# bool - float
r1 = True
r2 = 12.5
print(r1 < r2) # T
print(r1 > r2) # F
print(r1 == r2) # F
print(r1 != r2) # T
print(r1 >= r2) # F
print(r1 <= r2) # T
