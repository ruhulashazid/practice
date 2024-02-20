is_friend = True
is_user = False

if is_friend or is_user: #or operator#when you use or operator it will check if one of the condition is true
    print('Best friend forever') 
else:
    print('One of them')    
    
#Logical operator

print(4<5) #True

print(4>5) #False

print(4==5) #False
print(4!=5) #True
print(4<=5) #True
print('hello'=='hello') #True    


#another example

is_magician = True
is_expert = False

if is_expert and is_magician:
    print('you are a master magician')

elif is_magician or is_expert:
    print('at least you are getting there')    
    
elif is_magician and not is_expert:
    print('at least you are getting there')    
    