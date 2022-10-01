print("hi there 20!")

username='supercoder'
print(username)

long_string = '''
Its a long string
'''
print(long_string)

first_name=('Ruhul')
last_name=('Amin')
full_name=first_name+' '+last_name
print(full_name)

#string concatenation
print('hello'+' '+'Ruhul')
print('ruhul'+'3')


a = str(100)
b = int(a)
c = type(b)
print(c)


#Escape Sequence

weaher = "it's \"kind of\" sunny"
print(weaher)
weaher = "\t it's \"kind of\" sunny \n hope you have a good day"
print(weaher)

#formatted string

name = 'Ruhul'
print ('hi '+name)

age=22
print ('hi '+name + ' you are '+ str(age) + ' years old')

print(f'hi {name} you are {age} years old')#same as, it's work python3
print('hi {} you are {} years old'.format(name,age))#same as

print('hi {new_name} you are {new_age} years old'.format(new_name='Shazid',new_age='22'))#same as


#sring index

selfish = 'my no it'
         # 01234567
         
print(selfish)
print(selfish[0])
print(selfish[1])
print(selfish[2])
#[start:stop:stepover]
print(selfish[0:3])
print(selfish[0:8])
print(selfish[0:4:2])
print(selfish[:5])

s_a = '01234567'
     # 01234567
#[start:stop:stepover]
     
print (s_a[0:4]) 
print(s_a[::1])
print(s_a[:5])
print(s_a[::-1])#

s_a = s_a +'8'
print(s_a)


#lenth of string
greet = 'ruhul amin'

print(len(greet))#10
print(greet[0:len(greet)])
print(greet[0:10])




