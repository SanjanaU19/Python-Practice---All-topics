nums = [25, 10, 40, 15, 10, 50, 30, 20, 40]

print(len(nums))

print(dir(nums))

nums.append(100) # Add one element at end
print(nums)

nums.extend([35,45]) # Add multiple elements
print(nums)

nums.insert(1,15) # Add element at specific index -> nums(index,value)
print(nums)

nums.remove(10)  # Remove first occurrence of value
print(nums)

print(nums.pop()) # Remove and return element
print(nums)

print(nums.pop(1)) # list.pop(index) -> to remove particular index value

print(nums.index(50))  # Find index of an element

print(nums.count(40))  # Count occurrences of that value
print(nums.count(10))
print(nums.count(20))

l1 = nums.copy() # Create a copy of list
print(l1)
print(id(nums) == id(l1)) # false -> memory address should be different of both lists

print(nums.clear()) # Remove all elements

print(nums.sort()) # Sort the list
print(nums)

print(min(nums)) # return minimum value from the list
print(max(nums)) # # return maximum value from the list

print(sum(nums)) # print sum of all elements present in list


# nested list -> list inside list
array2d = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
          ]
print(array2d)
print(len(array2d)) # 3

for ele in array2d:
    print(ele)  # print [1, 2, 3] [4,5,6] [7,8,9]
    for el in ele:
        print(el) # 1 2 3 4 5 6 7 8 9