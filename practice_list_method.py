nums = [25, 10, 40, 15, 10, 50, 30, 20, 40]

# Q1. Add 60 at the end of the list.
nums.append(60)
print(nums)

# Q2. Add 70 and 80 to the list.
nums.extend([70,80])
print(nums)

# Q3. Add 5 at index 0.
nums.insert(0,5)
print(nums)

# Q.4 Remove the first occurrence of 10.
nums.remove(10)
print(nums)

# Q5. Remove the last element.
print(nums.pop())
print(nums)

# Q6. Find the index of 50.
print(nums.index(50))

# Q7. Find how many times 40 occurs.
print(nums.count(40))

# Q8. Sort the list in ascending order.
nums.sort()
print(nums)

# Q9. Sort the list in descending order.
nums.sort(reverse = True)
print(nums)

# Q10. Reverse the list.
nums.reverse()
print(nums)

# Q11. Find the largest number.
print(max(nums))

# Q12. Find the smallest number.
print(min(nums))

# Q13. Find the sum of all numbers
print(sum(nums))

# Q14. Find the length of the list.
print(len(nums))

# Q15. Create a copy of the list.
l1 = nums.copy()
print(l1)