import random
lst1 = [random.randint(1, 5) for i in range(5)]
print("List 1")
print(lst1)
lst2 = [random.randint(1, 5) for x in range(5)]
print("List 2")
print(lst2)
if lst1 != lst2:
    print("The lists are not equal")
elif lst1 == lst2:
    print("The lists are equal")
joinedlist = lst1 + lst2
print(joinedlist)
