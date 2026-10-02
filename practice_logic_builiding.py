# Q.1) Check whether a string has more than 5 characters.
s = input("Enter a string :")
n = len(s)

if len(s) > 5:
    print("The given string is long string")
else:
    print("not long string")

# Q.2) Check whether a string has exactly 10 characters.
s = "black"
if len(s) == 10:
    print(f"The {s} have exactly 10 character")
elif len(s) > 10:
    print(f"The {s} have more than 10 character")
else:
    print("The {s} have more than 10 character")

# Q . 3) whether all of these conditions are true:
# - String starts with "P"
# - Length is greater than 5
# - String ends with "n"
s = "Pen"
if s.startswith("P") and len(s) > 5 and s.endswith("n"):
    print("Valid")
else:
    print("Invalid")


# Q.4)  Check whether a string is empty or not.
s1 = input("Enter a string :")

if s1 == "":
    print("String is empty")
else:
    print("String is not empty")

#Q.5)Check whether the first character of a string is a vowel or consonant.
s1 = input("Enter a text :")
vowels = "aeiouAEIOU"

if s1[0] in vowels:
    print("First character is vowel")
else:
    print("First character is consonant")

#Q.6) Check whether the last character of a string is a vowel or consonant.
s1 = "Python"
vowels = "AEIOUaeiou"

if s1 == "":
    print("String is empty")
elif s1[-1] in vowels :
    print("The last character is vowel")
else:
    print("The last character is consonant")

#Q.7) Check whether a string starts with "A" or "a".
s = input("Enter a text:")

if s[0].lower() == "a" :
    print("String starts with a/A")
else:
    print("String does not starts with a/A")

#Q.8) Check whether a string ends with "ing" or not.
s = input("Enter a text:")
# print(s[-3:])  # ing
if s == "":
    print("String is empty")
elif s[-3:] == "ing":
    print("String ends with ing")
else:
    print("String does not end with ing")

# Q.9) Check whether a string contains a space or not.
s = input("Enter a text :")
s1 = " "
if s1 in s:
    print("String contains space")
else:
    print("String does not contain space")

# Q.10)Check whether a string contains a digit or not.
s1 = input("Enter a text :")
digits = "0123456789"

for char in s1: 
    if char in digits:
        print("String contains digit")
        break
else:
    print("String does not contain digit")

# Q.11)Check whether the first and last characters of a string are the same.
s = input("Enter a text :")

if s[0] == s[-1]:
    print("First and last character are same")
else:
    print("First and last character are different")

#Q.12) Check whether a string has more than 5 characters.
s1 = input("Enter a string : ")
if len(s1) > 5:
    print("String has more than 5 character")
elif len(s1) == 5:
    print("String has exact 5 character")
else:
    print("String has the less than 5 character")

#Q.13) Check whether the first character AND the last character of a string are both vowels.
s = input("Enter a text:")
vowels = "aeiou"

if s[0].lower() in vowels and s[-1].lower() in vowels:
    print("Both first and last character are vowels")
else:
    print("Both first and last character are consonant")

# Q.14) Check whether two strings are equal or not.
s1 = input("Enter a text1 :")
s2 = input("Enter a text2 :")

if s1 == s2:
    print("Both strings are equal")
else:
    print("Both strings are not equal")

# Q.15)Check whether two strings are equal ignoring uppercase/lowercase.
s1 = input("Enter a text1 :")
s2 = input("Enter a text2 :")

if s1.lower() == s2.lower():
    print("Strings are equal")
else:
    print("Strings are not equal")

# Q.16)Count the number of vowels in a string.
s1 = input("Enter a word :")
count = 0
vowels = "aeiou"
for char in s1.lower():
    if char in vowels:
        count += 1

print("The total count of vowels are : ", count)

# Q.17)Count the number of consonants in a string.
s1 = input("Enter a word:")
vowels = "aeiou"
count = 0

for char in s1.lower():
    if char.isalpha() and char not in vowels:
        count += 1

print("The total no.of consonant:",count)

# Q.18) Write a Python program to count the number of spaces in a string.
a = input("Enter a text :")
count = 0

for char in a: 
    if char == " ":
        count += 1

print("Total number of spaces : ", count)

# Q.19) Write a Python program to count how many times a particular character occurs in a string.
word = "ababababa"
target = "b"
count = 0

for char in word:
    if char == target:
        count += 1

print(f"Character {target} occurs {count} times")

# Question 20 — Find First Occurrence
# Write a Python program to find the index of the first occurrence of a given character in a string.
s = input("Enter a string :")
target = input("Enter a character :")

idx = s.find(target)

if idx != -1:
    print(f"First occurance of {target} is at index {idx}")
else:
    print(f"{target} is not present in string")

# # Question 21 — Reverse a String -> Write a Python program to reverse a string.
s = input("Enter a string : ")
reverse = " "

for char in range(len(s)-1,-1,-1):
    reverse = reverse + s[char]
print("The reverse string is:",reverse)

# # Question 22 — Palindrome String -> Write a Python program to check whether a string is a palindrome or not.
s = input("Enter a string :")
reverse = ""

for i in range(len(s)-1 , -1 ,-1):
    reverse = reverse + s[i]

if s == reverse:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")

# # Question 23 — Remove Spaces -> Write a Python program to remove all spaces from a string.
s = input("Enter a string:")
result = ""

for char in s:
    if char != " ":
        result = result + char
print("The string without spaces is :",result)

# Your next question — 24 -> Write a Python program to count the number of uppercase and lowercase characters in a string.
s = input("Enter a string :")
count_upper = 0
count_lower = 0

for char in s:
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1

print("Uppercase:",count_upper)
print("LowerCase:",count_lower)

# Question 25 -> Find the most frequent character in a string.
s = input("Enter a word:")

max_count = 0
freq_char = " "

for char in s:
    count = s.count(char)

    if count > max_count:
        max_count = count
        freq_char = char

print("character :",freq_char)

    

