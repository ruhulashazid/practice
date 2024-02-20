print("Hello World!")
x = 5
y = "I am shaneen"
print(x)
print(y)
#type declaratopn
z = str("Hello World")
print(z)
"""
"""
x,y,z="Blue", 7, "Green"
print(x)
print(y)
print(z)

#add 2 int value
a = 10
b = 2
print(a+b)

#add 2 string
p="Python is a"
q="programming language"
print(p+" "+q)

#Work to do
X = str("5")
Y = " Programming Language"
print(X+ Y)
#learing list
mylist=["Red","Green","Blue"]
print(mylist)
#specific value printing
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1],mylist[-2],mylist[0])
#shortcut
print(mylist[0:4])
mylist2=[1,2,"mango","red",5]
print(mylist2[0:])
print(mylist2[-5:])
#update any value
mylist2=[1,2,"mango","red",5]
print(mylist2)
mylist2[2]
print(mylist2)
mylist2[2:4] = ["Orange","apple"]
print(mylist2)


#finding length of string
mylist2=[1,2,"mango","red",5]
A=len(mylist2)
print(A)
#insert data in string
mylist2=[1,2,"mango","red",5]
mylist2.insert(3,"Orange")
print(mylist2)

#append
mylist2=[1,2,"mango","red",5]
mylist2.append("Orange")
print(mylist2)

#multiple string combined->extend
mylist2=[1,2,"mango","red",5]
mylist3=[3,4,5]
mylist2.extend(mylist3)
print(mylist2)

#muilenai abar krte hbe
a = [1,3,8]
b = ["S","H","A","N","E","E","N"]
c = ["A", "R", "A"]
a.extend(b)
print(a)
a.extend(c)
print(b)

#remove-->value likhte hbe
mylist=[1,2,"apple"]
mylist.remove(1)
print(mylist)
#pop--->index likhte hy
mylist=[1,2,"apple"]
mylist.pop(2)
print(mylist)
#clear-->full list khali kore dey
mylist=[1,2,"apple"]
mylist.clear()
print(mylist)
"""

#if else condition
"""
a!=b
a<b
a>b
a<=b
a>=b
"""

"""
#Check if which a<b?
a=5
b=10
if (a<b):
    print(str(a)+" is smaller than "+str(b))
else:
    print(str(b)+" is smaller than "+str(a))

#else if = elif
a=1
b=2
if (a<b):
    print(str(a)+" is less than "+str(b))
elif (a==b):
    print(str(a)+" is equal to "+str(b))
else:
    print(str(a)+" is greater than "+str(b))


#check is a is less than b and c
a=int(input())
b=int(input())
c=int(input())

if ((a<b) and (a<c)):
     print("a is less than b and c")
elif ((b<a) and (b<c)):
    print("b is less than a and c")
else:
    print("c is less than a and b") 

123  
a1=int(input())
b1=int(input())
c1=int(input())

if ((a1>b1) and (a1>c1)):
     print("a1 is greater than b1 and c1")
elif ((b1>a1) and (b1>c1)):
    print("b is greater than a and c")
else:
    print("c is greater than a and b")  


from matplotlib import pyplot as plt
X=[1,2,3]
Y=[2,4,1]
plt.plot(X,Y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("This is a graph")
plt.show()


"""
from matplotlib import pyplot as plt
X=[0,1,2,3,4]
Y=[1,3,5,7,9]
plt.plot(X,Y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("This is a graph")
plt.show()

#how to find oput which graph is which one
from matplotlib import pyplot as plt
X=[0,1,2,3,4]
Y=[1,3,5,7,9]
plt.plot(X,Y,label='graph1')
X1=[1,2,3]
Y1=[2,4,1]
plt.plot(X1,Y1,label='graph2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("This is a graph")
plt.legend()
plt.show()

#multiple sin(x)
from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(-np.pi,np.pi,200)
y=np.sin(x)
plt.plot(x,y,label="graph1")
plt.plot(x,2*y,label='graph2')
plt.plot(x,3*y,label='graph3')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("This is a graph")
plt.plot(x,y)
plt.legend()
plt.show()

#y=cos(x)
from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(-np.pi,np.pi,1000)
y=np.cos(x)
plt.plot(x,y,label="graph1")
plt.plot(x,2*y,label='graph2')
plt.plot(x,3*y,label='graph3')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("This is a graph")
plt.plot(x,y)
plt.legend()
plt.show()


#dotted line with range
from matplotlib import pyplot as plt
import numpy as np
X=[1,2,3,4,5]
Y=[1,3,5,7,9]
plt.plot(X,Y,color='blue',linestyle='dashed',linewidth=4,marker='o',markerfacecolor='pink',markersize=15)
plt.xlim(1,15)
plt.ylim(0,10)
plt.show()

# special character replace
txt = "Hello!!! This% is & python*,; language";

txt.replace("!", "")
txt.replace("%", "")
txt.replace("&", "")
txt.replace(",", "")
txt.replace("*", "")
txt.replace(";", "")

# recursion
def find_largest(nums):
    if len(nums) == 1:
        return nums[0]
    
    largest_number = find_largest(nums[1:])
    
    if nums[0] > largest_number:
        return nums[0]

    return largest_number

def find_smallest(nums):
    if len(nums) == 1:
        return nums[0]
    
    smallest_number = find_largest(nums[1:])
    
    if nums[0] < largest_number:
        return nums[0]

    return smallest_number


find_largest([0, 2, 1])

#matplotlib sec1
import matplotlib.pyplot as plt
x1 = [0, 1, 2, 3]
y1 = [3, 8, 1, 10]
plt.subplot(1,2,1)
plt.plot(x1, y1, label = 'graph 1', color = 'red', linestyle = ':')
plt.legend()

x2 = [0, 1, 2, 3]
y2 = [10, 20, 30, 40]
plt.subplot(1,2,2)
plt.plot(x2, y2, label = 'graph 2', color = 'red', linestyle = ':')

plt.legend()
plt.show()

#matplotlib sec2
from matplotlib import pyplot as plt
import numpy as np
x1=np.array([0,1,2,3])
y1=np.array([3,8,2,10])
x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])
x3=np.array([1,2,3])
x4=np.array([1,2,3])
y3=np.array([4,1,3])
plt.subplot(2,3,1)
plt.plot(x1,y1)
plt.title('First Graph')
plt.subplot(2,3,2)
plt.plot(x2,y2)
plt.title('Second Graph')
plt.subplot(2,3,3)
plt.plot(x3,y3,x4)
plt.title('Third Graph')
plt.show()




# matrix
a= [
2, 5, 7
6, 2, 12
10, 14, 11
]

b = [
13, 3, 2
6, 2, 12
10, 14, 11
]


output = [
2, 5, 7
6, 9, 12
10, 14, 11
]

Example: To print the matrix
M1 = [[8, 14, -6], 
           [12,7,4], 
           [-11,3,21]]

#To print the matrix
print(M1)

Example 2: To read the last element from each row.
M1 = [[8, 14, -6],
           [12,7,4], 
           [-11,3,21]]

matrix_length = len(M1)

#To read the last element from each row.
for i in range(matrix_length):
    print(M1[i][-1])

Example 3: To print the rows in the Matrix
M1 = [[8, 14, -6],
           [12,7,4], 
           [-11,3,21]]

matrix_length = len(M1)

#To print the rows in the Matrix
for i in range(matrix_length):
    print(M1[i])

#matrix avg
M1 = [[6, 14, -6], 
      [12,13,4], 
      [-11,3,21]]

M2 = [[2, 16, -6],
           [9,5,-4], 
           [-1,3,13]]

M3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]
matrix_length = len(M1)

#To Add M1 and M2 matrices
for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k] = M1[i][k]/2 + M2[i][k]/2

#To Print the matrix
for row in M3:
    print(f"{row[0]} {row[1]} {row[2]}")


#using numpy
import numpy as np

M1 = np.array([[3, 6, 9], [5, -10, 15], [-7, 14, 21]])
M2 = np.array([[9, -18, 27], [11, 22, 33], [13, -26, 39]])
M3 = M1/2 + M2/2  
print(M3)
#multipli
import numpy as np

M1 = np.array([[3, 6], [5, -10]])
M2 = np.array([[9, -18], [11, 22]])
M3 = M1.dot(M2)  
print(M3)

#transpose
import numpy as np

M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
M2 = M1.transpose()

print(M2)


#first--->sign remove
val = "Hello!!!This @ is a, .;'python % & program"
counter=0
length = len(val)
my_val = list(val)
for i in range (0,length):
    if(my_val[i] == '!' or my_val[i] == '%'):
        my_val[i] = '*'
        counter=counter+1
    elif(my_val[i] == '`'):
        my_val[i] = '*'
        counter=counter+1
for i in range(0,length):
    print(my_val[i],end="")
print()
print("Number of signs without *:",counter)

#second---->larger number
xx = int(input("Enter x: "))
yy = int(input("Enter y: "))
zz= int(input("Enter z: "))
if xx > yy and xx > zz:
    print("X is the largest number")
elif yy > xx and yy > zz: 
    print("Y is the largest number")
else:
    print("Z is the largest number")

#third--->matrix
A=[ [6,12,8], [4,4,10], [6,0,16] ]
B=[ [2,16,4], [8,10,0], [14,8,6] ]
C=[]
for i in range(len(A)):
    C.append([])
    for j in range(len(A[0])):
        C[i].append(A[i][j]+B[i][j])
print("C=",C)

#fourth-->matplotlib
from matplotlib import pyplot as plt
import numpy as np
x1=np.array([0,1,2,3])
y1=np.array([3,8,2,10])
x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])
x3=np.array([1,2,3])
x4=np.array([1,2,3])
y3=np.array([4,1,3])
y4=np.array([2,4,0])
plt.subplot(2,3,1)
plt.plot(x1,y1)
plt.title('First_one')
plt.subplot(2,3,2)
plt.plot(x2,y2)
plt.title('Second_one')
plt.subplot(2,3,3)
plt.plot(x3,y3,x4,y4)
plt.title('Third_one')
plt.show()
"""

 
    

   
