#iterable _ can be iterated over
#iterable is an object that can return an iterator
#iterable is an object that can be used in a for loop
#iterable _one by one chack each item in the collection 

Users = { 
        'name': 'sun',
        'age': 23,
        'is_student': False
        }

for item in Users.items():
    print(item)
    
for item in Users.values():
    print(item)

for item in Users.keys():
    print(item)    

for k,v in Users.items():
    print(k,v)
    
    
    
#counter 
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

for item in my_list: 
    counter = 0
    counter = counter + item
print(counter)