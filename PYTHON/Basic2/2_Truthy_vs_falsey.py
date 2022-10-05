#Truthy and Falsey

is_old = bool('hello')
is_licensed = bool(5)

if is_old and is_licensed: 
    print("You are old enough to drive and you have a license !")
       
else:
    print("You are not old enough to drive")  
    print('ok')   

#another example

password= '12345'
username= 'ruhul'

username = input('Enter your username: ')
password = input('Enter your password: ')

if password == '12345' and username == 'ruhul':
    print('you are logged in')
else:
    print('invalid username or password')
    
#Ternary operator

is_friend = False #True  #change this to see the result

can_message ="message allowed" if is_friend else "not allowed to message" 

print (can_message)
    
        