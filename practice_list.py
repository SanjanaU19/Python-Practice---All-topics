# Question 1 -> Write a Python program to find the largest element in a list.
nums =  [10, 25, 7, 40, 15]
largest = nums[0]
for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i+1]
print("Largest element of list is : ",largest)


# Question 2 — Write a Python program to find the smallest element in a list.
nums = [10, 25, 7, 40, 15,6]
smallest = nums[0]

for i in range(len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
print("The smallest value of nums is:",smallest)


# Question 3 — Write a Python program to find the sum of all elements in a list.
nums = [10, 20, 30, 40,50]
total = 0

for i in range(len(nums)):
    total += nums[i]
print("The total sum of all elements in nums is:",total)


# Question 4 — Write a Python program to count how many even and odd numbers are present in a list.
nums =  [10, 7, 4, 9, 12, 5,8,15,19]
count_even = 0
count_odd = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Total no.of even :",count_even)
print("Total no.of odd :",count_odd)


# Question 5 — Write a Python program to find the largest and smallest element in a list without using max() or min().
nums = [15, 8, 27, 3, 19,100]
largest = nums[0]
smallest = nums[0]

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    elif nums[i] < smallest:
        smallest = nums[i]
print("The largest element of nums is:",largest)
print("The smallest element of nums is:",smallest)


# Question 6 — Write a Python program to count how many times a particular number occurs in a list.
nums = [10, 20, 10, 30, 10, 40,20,60,10]
count = 0
target = int(input("Enter a number:"))

for num in nums:
    if nums[num] == target:
        count += 1
print(f"{target} occur {count} times")


# Question 7 —> Write a program to find all numbers greater than 10 in a list.
nums = [5, 15, 8, 20, 3, 25,12,17]
l1 = []
for num in nums:
    if num > 10:
        l1.append(num)
print("The number greter than 10 is :",l1)


# Question 8 — Write a Python program to create a new list containing only the even numbers from a given list.
nums = [10, 7, 4, 9, 12, 5,6,1,8]
output = []

for num in nums:
    if num % 2 == 0:
        output.append(num)
print("The list of total even number:",output)


# Question 9 — Write a Python program to create a new list containing only the odd numbers from a given list.
nums = [10, 7, 4, 9, 12, 5,6,1,8]
output = []

for num in nums:
    if num % 2 != 0:
        output.append(num)
print("The list of total odd number:",output)


# Question 10 - Find the sum of all even numbers in the list.
nums = [10, 7, 4, 9, 12, 5,6,2]
total = 0

for num in nums:
    if num % 2 == 0:
        total += num
print("Total of all even number:",total)
# even = []  # 2nd solution
# total = 0
# for num in nums:
#     if num % 2 == 0:
#         even.append(num)       
# for i in range(len(even)):
#     total += even[i]
# print("Total of all even number:",total)

# Question 10 — Reverse a list without using reverse() or slicing [::-1].
nums = [10, 20, 30, 40, 50]
reverse = []

for i in range(len(nums)-1,-1,-1):
    reverse.append(nums[i])
print("Reverse :",reverse)


# Question 11 — Write a Python program to find the second largest element in a list.
nums = [10, 25, 7, 40, 15]
largest = nums[0]
second_lrg = nums[0]

for i in range(len(nums)):
    if nums[i] > largest:
        second_lrg = largest
        largest = nums[i]
    
    elif nums[i] > second_lrg:
        second_lrg = nums[i]
print("Largest :",largest)
print("Second_largest:",second_lrg)


# Question 12 — Write a Python program to find the second smallest element in a list.
nums = [10, 25, 7, 40, 15,2]
smallest = nums[0]
second_smallest = nums[0]

for i in range(2,len(nums)):
    if nums[i] < smallest:
        second_smallest = smallest
        smallest = nums[i]

    elif nums[i] < second_smallest:
        second_smallest = nums[i]
print("Smallest :",smallest)
print("Second Smallest :",second_smallest)


# Question 13 — Write a Python program to remove duplicate elements from a list without using set().
nums = [10, 20, 10, 30, 20, 40,50,]
output = []

for num in nums:
    if num not in output:
        output.append(num)
print(output)


# Question 14 — Write a Python program to find the common elements between two lists.
nums1 = [10, 20, 30, 40,50,70]
nums2 = [20, 40, 50, 60,70,80]

res = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
print("The common elemnet from both list are:",res)


# Question 15 — Write a Python program to find the duplicate elements in a list.
nums = [10, 20, 10, 30, 20, 40, 10,40]
duplicates = []

for i in range(len(nums)):
    if nums.count(nums[i]) > 1 and nums[i] not in duplicates:
        duplicates.append(nums[i])

print("Duplicate element from nums :",duplicates)


# Question 16 — Write a program to find the sum of all numbers greater than 10.
nums =  [5, 15, 8, 20, 3, 25,50]
total = 0

for i in range(len(nums)):
    if nums[i] > 10:
        total += nums[i]

print("The sum of all digits greter than 10 is:",total)