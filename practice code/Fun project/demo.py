#Solution1
This_string = "Hello!!! This@ is a ,;'python%& prog(ram"
Unvalide_string= "!@%&*()_+|:<>?/.,;'[]\=-`~"
for char in Unvalide_string:
    This_string = This_string.replace(char, "")

print(This_string[::-1] )


#Solution2
number = int(input ("Enter the number : "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)    


#Soution3

