lst=[10,20,30,80,2,1]

lst.sort() #sort the list
print(lst)

print("max")  #print maximum of a list
print(max(lst))

print("min")
print(min(lst)) #print minimum of the list

print("appended")
lst.append(2) # append the end of list
print(lst)

print("insert") # insert the item to specific index
lst.insert(1,20)

print("extend") #extend the list
lst1=[1,20,30]

lst.extend(lst1)
print(lst)

print("COUNT OF 1") #print the len of list
print(lst.count(1))

print(len(lst))


# how find index of an item 
print(lst.index(20))
