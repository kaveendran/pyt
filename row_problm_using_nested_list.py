#create rows
grid=[[1,0,0],[0,0,0],[0,0,0]]

#printing organized grid

print("{}\n{}\n{}".format(grid[0],grid[1],grid[2]))

grid_selection=input("Enter Your Grid Selection(Row,Column) : ")

# editing grid formation
row=int(grid_selection[0])-1
column=int(grid_selection[1])-1
grid[row][column] =1




#outputying grid formation
print("{}\n{}\n{}".format(grid[0],grid[1],grid[2]))
