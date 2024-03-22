#enumerate() function returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over sequence.

for i, chir in enumerate('Python'):
    print(i, chir)

for i, chir in enumerate((1, 2, 3, 4, 5)):
        print(i, chir)
        
for i, chir in enumerate(list(range(100))):
    print (i,chir)
    if chir == 20:
        print(f'index of 20is: {i}')
