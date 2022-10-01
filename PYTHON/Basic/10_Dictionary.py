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
print('age' in user.keys())
print('age' in user.values())
print('hello' in user.values())


