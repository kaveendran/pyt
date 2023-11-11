# nested list can be use in python 

# nested list is a list inside a list [1,2,[1,2,3],5,6]
nstd_lst=[10,20,[20,50,30,40],50,90,60]

# her we are going to see the index of list inside a list

print(nstd_lst.index([20,50,30,40]))

# so here we can see the index of this inner list is 2

# we can do slicing in this nested list 

print(nstd_lst[0:2])
# here we can see the nested list slicing operation 

# how access inner list 

print(nstd_lst[2][0])

# in here we are using inner list index [0]

# we can also slice the inner list also 



