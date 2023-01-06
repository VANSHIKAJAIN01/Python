#create an empty set
s = set()

#add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

#add 3 one more time
s.add(3)

#remove an element
s.remove(2)
print(s)

print(f"The set has{len(s)} elements")
#len func gives us the length of data structure