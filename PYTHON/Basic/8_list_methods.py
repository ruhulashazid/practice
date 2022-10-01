#list methods
basket = [1,2,3,4,5]
#adding
basket.append(100)
new_list = basket
print (new_list)
print (basket)

#removing
basket = [1,2,3,4,5]
basket.pop(4)
print(basket)

basket = [1,2,3,4,5]
basket.remove(4)
print(basket)

basket = [1,2,3,4,5]
new_list = basket.clear()
print (basket)

#indexing
basket = [1,2,3,4,5]
print (basket.index(4))

basket =['a','x','b','c','d','e','d']
print(basket.index('d'))
print('d' in basket)
print('x' in basket)
print('i' in basket)
print(basket.count('d'))

#sorting

basket=['a','x','b','c','d','e','d']

#basket .sort()

print(sorted(basket))
print(basket)

#reverse

basket=['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print(basket)
