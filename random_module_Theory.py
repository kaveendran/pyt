import random   #importing random module 


# randint(a,b)  range >>>> (a<= x <=b)
# randrange(a,b) range >>>> (a<= x <b)
# random() range >>>> (0.0<= x <1.0)
# uniform()
# choice() # select particular item from list or tuple
# shuffle() # shuffle any sequence

a=random.randint(1,3)
print(a)

b=random.randrange(1,3)
print(b)

c=random.random()
print(c)

d=random.uniform(1,3)
print(d)

lst=[1,2,3,4]
e=random.choice(lst)
print(e)


random.shuffle(lst)
print(lst)