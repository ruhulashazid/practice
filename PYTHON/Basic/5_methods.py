qout = 'to be not to be '

print (qout.upper())
print(qout.capitalize())

qout2 = qout.replace('be','me')
print(qout2)

qout = 'TO BE NOT TO BE '
print(qout.lower())

#booleans

name = 'Ruhul'

is_cool = False
is_cool = True

print(bool(1))
print(bool(0))


#simple 
name = 'Ruhul amin'
age = 22
relationship_status = 'single'
print(relationship_status)

relationship_status = 'it\'s complicated'
print(relationship_status)

#complex

birth_year = input('what year were you born?')

age = 2022 - int(birth_year)
print (f'your age is {age}')


#exercise#password checker
user_name = input('what is your name?')
password = input('what is your password?')

#print (f'your name is {user_name} and your password is {password}')
print (f'your name is {user_name} and your password is {password} length is {len(password)}')

password_length = len(password)
hiddent_password = '*' * password_length
print(f'{user_name}, your password {hiddent_password} is {password_length} letters long')
#end of exercise






