marks = int(input("Enter a marks : "))

if marks <= 100 and marks >= 90:
    print("The grade is A")
elif marks <= 89 and marks >= 75:
    print("The grade is B")
elif marks <= 74 and marks >= 60:
    print("The grade is C")
elif marks <= 59 and marks >= 40:
    print("The grade is D")
else:
    print("The student is Fail ")

# 10. Simple Calculator ⭐
# Take two numbers and an operator from the user.

num1 = int(input("Enter a number1 :"))
num2 = int(input("Enter a number2 :"))
operator = input("Enter a operator :")

if operator == "+":
    print("Addition of two number is :" ,num1 + num2)
elif operator == "-":
    print("Substraction of two number :" ,num1 - num2)
elif operator == "*":
    print("Multiplication of two number is : ",num1 * num2)
elif operator == "/":
    print("Division of two number is :" ,num1 / num2)
elif operator == "%":
    print("The modulus of two number is :",num1 % num2)
elif operator == "//":
    print("The floor division of two number is :",num1 // num2)
else:
    print("Invalid operator")

# 1. Check Positive, Negative or Zero

num = int(input("Enter a number : "))

if num > 0 :
    print(f"{num} is positive")

elif num < 0 :
    print(f"{num} is Negative")

else:
    print(f"{num} is zero")


# 2. Check Even or Odd
num = int(input("Enter a number : "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 3. Check Voting Eligibility
# Take age as input.
# Age ≥ 18 → "Eligible to vote"
# Otherwise → "Not eligible to vote"

age = int(input("Enter a number : "))

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not eligible for Voting")


# 4. Find Greater Number
# Take two numbers and print which number is greater
num1 = int(input("Emter a num1 : "))
num2 = int(input("Enter a num2 : "))

if num1 > num2 :
    print(f"The {num1} is Greater than {num2} ")

else:
    print(f"The {num2} is Greater than {num1}")

# 5. Find Greatest Among Three Numbers
n1 = int(input("Enter a first number :"))
n2 = int(input("Enter a second number :"))
n3 = int(input("Enter a third number : "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is greater than {n2} and {n3}")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is greater than {n1} and {n3}")
else:
    print(f"{n3} is greater than {n1} and {n2}")

# 6. Check Pass or Fail
marks = int(input("Enter a marks : "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 8. Check Leap Year ⭐
# Take a year and check whether it is a leap year.
year = int(input("Enter a year : "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"The {year} is Leap")
else:
    print(f"The {year} is not leap")


# 9. Check Divisibility
# Take a number and check:
# Divisible by both 3 and 5
# Divisible only by 3
# Divisible only by 5
# Not divisible by either

num = int(input("Enter a number :"))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by 3 & 5")
elif num % 3 == 0:
    print(f"{num} is divisible by 3")
elif num % 5 == 0:
    print(f"{num} is divisible by 5")
else:
    print("Invalid")


1.Check Character Type
# Take one character and check whether it is:
# Uppercase letter
# Lowercase letter
# Digit
# Special character

s1 = input("Enter a text :")

if s1.isupper():
    print(f"The given {s1} is in upperCase")
elif s1.islower():
    print(f"The given {s1} is in lowerCase")
elif s1.isdigit():
    print(f"The given {s1} is in digit")
else:
    print(f"The given {s1} is speacial character")


# 2.Electricity Bill
# Calculate the bill based on units:
# 0--100 units → ₹5/unit
# 101--200 → ₹7/unit
# Above 200 → ₹10/unit

units = int(input("Enter a units :"))
if units < 0:
    print("Invalid")
elif units <= 100 and units > 0:
    print("The total cost of units as 5rs per unit is :" ,units * 5)
elif units <= 200 and units >= 101:
    print("The total bill is per unit 7rs/units.",units * 7)
else:
    print("Total bill is per unit 10rs/unit : ",units * 10)

# 3. Login System ⭐
# Take username and password.

username = "admin1234"
password = "1234"

if username == "admin1234" and password == "1234":
    print("Login Successful.....")
else:
    print("Invalid Username or password.....")

# if nested statement
age = int(input("Enter a age :"))
salary = int(input("Enter a salary amount :"))

if age >= 18 :
    if salary >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")
else:
    print("Age is not eligible")

# Task There are 3 friends with some age. WAP to print who will pay the bill?
jay = 22    
viru = 23
basanti = 21

if jay > viru and jay > basanti:
    print("jay will pay the bill")

elif viru > jay and viru > basanti:
    print("Viru will pay the bill")

else:
    print("Basanti will pay the bill")

# ### Task-2 
### You have given a number. num = 15
### WAP to check following conditions 
    # 1. if number is divisible by 3 display "FIZZ"
    # 2. if number is divisible by 5 display "BUZZ
    # 3. if number is divisible by 3 & 5 both display "FIZZBUZZ"
#  num = 15   ---> FIZZBUZZ
#  num = 10    ----> BUZZ

n = 24
if n % 3 == 0 and n % 5 == 0:
    print("FIZZBUZZ")

elif n % 3 == 0:
    print("FIZZ")

elif n % 5 == 0:
    print("BUZZ")

else:
    print("Invalid")

