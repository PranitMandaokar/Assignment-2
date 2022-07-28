# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(f'before sorting {a}')

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][1] < a[j][1] :
          # swapping logic  
           c = a[i]
           a[i] = a[j]
           a[j] = c

print(f'after sorting  {a}')
