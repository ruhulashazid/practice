#tuple has only two methods: count and index

my_tuple = (1,2,3,4,5)
print (5 in my_tuple)
user = {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20  
}

print (user.items())
user = {
    (1,2):[1,2,3],
    'greet':'hello',
    'age':20  
}

print(user[(1,2)])


####################

my_tuple = (1,2,3,4,5,5,5)
x= my_tuple[0]
y= my_tuple[1]
print (x)

#sort() 
x,y,z,*other = (1,2,3,4,5)

print (x)
print(*other)
print(z)

print (my_tuple.count(5))
print (len(my_tuple))