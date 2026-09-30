# right triangle
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# Inverted triangle
n = 6
for i in range(n,-1,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# Pyramid
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    
    for j in range(2*i-1):
        print("*",end="")
    print()

# Diamond
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    
    for j in range(2*i-1):
        print("*",end="")
    print()

for i in range(n,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    
    for j in range(2*i-1):
        print("*",end="")
    print()

# Butterfly 
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")

    for j in range(2*(n-i)):
        print(" ",end="")

    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(n,-1,-1):
    for j in range(1,i+1):
        print("*",end="")

    for j in range(2*(n-i)):
        print(" ",end="")
    
    for j in range(1,i+1):
        print("*",end="")
    print()

# Floyd's Triangle ⭐
n = 5
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num += 1
    print()

# Increasing number triangle
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Decreasing number pattern
n = 5
for i in range(n,-1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Same number in each row
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()


# Number pyramid
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for j in range(2*i-1):
        print(j + 1,end="")

    print()

0-1 pattern
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i + j) % 2 , end="")
    print()

Hollow square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j ==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

Hollow Triangle
n = 6
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == 1 or j == i or i == n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Pascal's triangle

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    num = 1
    for j in range(i+1):
        print(num,end=" ")
        num = num *(i - j) // (j+1)
    print()