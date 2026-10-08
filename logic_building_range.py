# 1. Print numbers from 1 to 50.
for i in range(1,51):
    print(i,end= " ")

# 2. Print all even numbers from 1 to 50.
for i in range(1,51):
    if i % 2 == 0:
        print(i,end=" ")
    
# 3. Print all odd numbers from 1 to 50.
for i in range(1,51):
    if i % 2 != 0:
        print(i,end=" ")

# 4. Print numbers from 50 to 1.
for i in range(50,0,-1):
    print(i,end=" ")
  
# 5. Print the multiplication table of a number.
n = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n} * {i} = {n * i}")

# 6.Find all numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end = " ")


# 7. Find pairs of numbers whose sum is equal to a given number.
num = [2, 4, 3, 5, 7, 8]
target = 10

for i in range(1,len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == target:
            print(f"The first number is : {num[i]} ,The second number is : {num[j]}")

# 8.Find the element that appears only once in a list.
numbers = [4, 2, 7, 2, 4, 9, 7, 5, 9]

for i in range(len(numbers)):
    if numbers.count(numbers[i]) == 1:
        print(numbers[i])

# 9.Find the largest number in a list without using max().
nums = [23, 7, 45, 12, 89, 34, 56]
n = len(nums)
largest = nums[0]

for i in range(n-1):
    if nums[i] > largest:
        largest = nums[i]
print("The largest number of the list is :",largest)

# 10.Find the smallest element in the list without using min().
nums = [23, 7, 45, 12, 89, 34, 56]
smallest = nums[0]

for i in range(1,len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
print(f"The smallest element of list is : {smallest}")

# 11. Find the sum of all elements in a list without using sum().
nums = [10, 20, 5, 15, 30]
sum = 0

for i in range(len(nums)):
    sum += nums[i]
print(f"Sum of all elements from the list is : {sum}")

# 12. Count how many even and odd numbers are present in a list.
nums = [12, 7, 5, 18, 20, 9, 14, 3]

even_count = 0
odd_count = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0 :
        even_count += 1
    else:
        odd_count += 1

print("The count of all even numbers in the list:",even_count)
print("The count of all odd numbers in the list:",odd_count)

# 13.Print only the positive numbers from this list.
nums = [-5, 10, -2, 8, 0, -7, 15, 3]

for i in range(0,len(nums)):
    if nums[i] > 0:
        print(nums[i],end=" ")

# 14. Reverse a list without using reverse() or [::-1].
nums = [10, 20, 30, 40, 50]
reverse = []
n = len(nums)
for i in range(n-1,-1,-1):
    reverse.append(nums[i])
print(f"The reverse of the list is : {reverse}")

# 15. Count how many times a particular number appears in a list — without using .count().
nums = [2, 5, 3, 2, 8, 2, 5, 9, 2]
target = 2
count = 0

for i in range(len(nums)):
    if nums[i] == target:
        count += 1

print(f"The {target} appears {count} times")

16.Find the second largest element in a list without using sort() or max().
nums = [12, 45, 7, 89, 34, 56, 23]

largest = nums[0]
second_largest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest:
        second_largest = nums[i]

print(f"The second largest number is: {second_largest}")

# 17.Find all duplicate elements in a list.
nums = [2, 5, 7, 2, 8, 5, 9, 7, 3]
duplicates = []

for i in range(len(nums)):
    if nums.count(nums[i]) > 1 and nums[i] not in duplicates:
        duplicates.append(nums[i])
print(duplicates)

# 18.Find all duplicate elements in a list. -- do it without using count()
nums = [2, 5, 7, 2, 8, 5, 9, 7, 3]
duplicates = []
count = 0

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            duplicates.append(nums[i])
print(duplicates)

# 19.Find the common elements between two lists without using set().
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []
# 1st method
for num in list1:
    if num in list2:
        common.append(num)
print(common)

# 2nd method
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            common.append(list1[i])
print(common)

# 20.Remove duplicate elements from a list without using set().
nums = [2, 4, 2, 5, 4, 7, 5, 8]
n1 = []

for i in range(0,len(nums)):
    if nums.count(nums[i]) >= 1 and nums[i] not in n1:
        n1.append(nums[i])
print(n1)