#set is a un ordered collection of unique items

my_set={1,2,3,4,5,5}
my_set.add(100)#add 100 to the set
my_set.add(2)#it will not add 2 because it is already in the set
print (my_set)#it will print {1,2,3,4,5,100}

my_list = [1,2,3,4,5,5]
print (set(my_list))#convert list to set

my_set= {1,2,3,4,5,5}

new_set= my_set.copy()
my_set.clear()
print (new_set)#it will print {1,2,3,4,5}
print(my_set)#it will print set()

############################################
my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}
print (my_set.difference(your_set))#it will print {1,2,3}
print (my_set.discard(5))#it will remove 5 from the set
print(my_set)#it will print {1,2,3,4}it will not print 5 because it is already removed
print(your_set.difference(my_set))#it will print {6,7,8,9,10}
print (my_set)

#union
my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.union(your_set))#it will print {1,2,3,4,5,6,7,8,9,10}
print (my_set | your_set)#it will print {1,2,3,4,5,6,7,8,9,10}#same as above

#issubset
my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}

print (my_set.issubset(your_set))#it will print false#because my_set is not a subset of your_set


#intersection   

my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}
print (my_set.intersection(your_set))#it will print {4,5}
print (my_set & your_set)#it will print {4,5}#same as above

#superset

my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}

print (my_set.issuperset(your_set))#it will print false#because my_set is not a superset of your_set