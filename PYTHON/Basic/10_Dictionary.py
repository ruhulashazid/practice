dictionary = {
    'a':1,
    'b':2,
    'x':3
    
}

#print(dictionary['a'])
#print(dictionary['c'])#error
#print(dictionary)

#another example its a list
my_list = [
   {
    'a':[1,2,3],
    'b':['hello'],
    'x':True
   },{
    'a':[4,5,6],
    'b':['bye'],
    'x':True
   }

]


#dictionary methods
user = {
    'basket':[1,2,3],
    'greet':'hello'
}

print (user.get('age',55))

user2 = dict(name='ruhul')
print(user2)

#another example
user = {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20  
}

print('basket' in user)
print('age' in user.keys())#same as above
print('age' in user.values())#it will return false because it is not in the values
print('hello' in user.values())#it will return false because hello is not in the values


user2= user.copy()
print (user.clear())
print (user2)#it will print the copy of user
user = {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20  
}
print (user.pop('age'))
print (user)#


user = {
    'basket':[1,2,3],
    'greet':'hello',
    'age':20  
}

print(user.update({'age':55}))#it will update the age
print(user)

print(user.popitem())#it will remove the last item
print(user)
