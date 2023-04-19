



def find_common(list1, list2, list3):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
     
    # Use list comprehension to find common elements
    # in all three sets and return as a list
    return [elem for elem in set1 if elem in set2 and elem in set3]
n = 100000
triangle = [int(i*(i+1)/2) for i in range(1,n)]
pentagonal = [int(i*(3*i-1)/2) for i in range(1,n)]
hexagonal = [int(i*(2*i-1)) for i in range(1,n)]

print(find_common(triangle,pentagonal,hexagonal))