# WAP to check number is prime or not
n = int(input("Enter a number:  "))

prime = True
if n <= 1:
    print(f"{n} is not prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            prime = False

if prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")

# WAP to print all prime numbers
for n in range(2,100):
    prime = True

    for i in range(2,n):
        if n % i == 0:
            prime = False

    if prime:
        print(n,end=" ")
