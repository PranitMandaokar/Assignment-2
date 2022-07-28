# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# logic -1

dict_1 = {}
aplhabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = len(aplhabets) 
i = 0
while i < count:
   dict_1[aplhabets[i]] = (ord(aplhabets[i]))
   i += 1

print(dict_1)

# logic -2 ()

dict_1 = {}
aplhabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = len(aplhabets) 
i = 0
while i < count:
   dict_1[aplhabets[i]] = (ord('a')+i)
   i += 1

print(dict_1)
