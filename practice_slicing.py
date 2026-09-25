s = "Instagram"

# print Insta 
print(s[0:5:+1])
print(s[:5])  # another method

# print gram 
print(s[5:len(s):+1])
print(s[5:])

# print s in positive indexing -> Instagram
print(s[:])
print(s[0:len(s):+1])
print(s[ : : ])

# print from negative indexing -> margatsnI
print(s[ : :-1])
print(s[-1:-10:-1])
print(s[::-1])

print(s[-1:8:-1]) # print empty string
