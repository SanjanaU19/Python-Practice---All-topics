name = "Sanjana Umate"

# print 1st name -> Sanjana 
print(name[0:8])

# print name skip 1 letter -> ajn 
print(name[1:8:2])

# print the whole string -> Sanjana Umate
print(name[0:13])

# print 1st name if index start from zero there is no need to define the Zero python by default consider it
print(name[:8])

# print whole string in backword direction
print(name[::-1])

# print whols string consider name[0:len(name)]
print(name[:])

# print umate only
print(name[8:13])

# print only umate they consider stop condition by default is len(name)
print(name[8:])

# print sanja 
print(name[0:5:1])

# print Umat 
print(name[-5:-1:1])

# print umate in backword direction -> etamU
print(name[-1:-6:-1])

# print sanjana in backword direction -> anajnaS
print(name[-7:-14:-1])

# print etamU anajna
print(name[-1:-13:-1])

# print etamU anajnaS
print(name[-1:-13-1:-1])

# print 1 letter skip in negative direction -> eaUaanS
print(name[-1:-14:-2])

# print umate -> u a e only
print(name[8:len(name):2])

# print by skipping 3 letter from name
print(name[0:len(name):3])

# print all name by using space 
print(*name[0:len(name):1]) 

# print all name in backword index usig space
print(*name[len(name):0:-1])

# print all odd index only
print(name[1:len(name):2])

# print all evem index  
print(*name[0:13:2])  # * used to create space between slicing output

# Print characters from index 3 to 10 -> jana Um
print(name[3:10])

# Print the last 4 characters backward
print(name[-1:-5:-1])
