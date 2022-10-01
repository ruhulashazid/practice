li = [1,2,3,4,5,6,7,8,9,10]
li = ['a','b','c','d','e','f','g','h','i','j']
li3 = [1,2,3.2,'a','b','c',True,False]

#more examples
amazon_cart = ['notebooks','sunglasses','toys','grapes']
print(amazon_cart[0])
print(amazon_cart[1])
print (amazon_cart[2])
print (amazon_cart[3])

#List slicing

amazing_cart = ['notebooks',
                'sunglasses',
                'toys',
                'grapes'
                ]
print (amazing_cart[0:2])

#next example
amazon_cart = ['notebooks',
                'sunglasses',
                'toys',
                'grapes'
                ]

amazon_cart[0] ='laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print (new_cart)
print (amazon_cart)

