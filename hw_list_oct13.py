# WAP to get all unique elemnt list from nums without changing position
nums = [5,4,5,4,6,7,8,4,3,5,3,4]
duplicates = []

for num in nums:
    if nums.count(num) >= 1 and num not in duplicates:
        duplicates.append(num)
    
print("The list of all unique numbers:",duplicates)
print(len(duplicates))

# Find freq of every elemnet from above list in dict
nums = [5,4,5,4,6,7,8,4,3,5,3,4]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Frequency of all elemnts :",freq)

# Find freq of every elemnet from string in dict
s = "I love python programming"
freq1 = {}
for char in s:
    if char in freq1:
        freq1[char] += 1
    else:
        freq1[char] = 1
print(freq1)

# find who is absent for which paper
db = {"name" : ["jay","Raj","Riya"],
       "marks" : [[78,67,"AB"],[98,"AB",81],["AB","AB",99]],
       "sub":["Maths","Python","English"]
    }
    
for i in range(len(db["name"])):
    for j in range(len(db["sub"])):
        if db["marks"][i][j] == "AB":
            print(db["name"][i] ,"is absent for",db["sub"][j])



    