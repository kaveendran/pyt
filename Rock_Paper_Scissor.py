import random

print("ROCK PAPER SCISSOR")
game_st=input("Start/Quit :")
game_st = game_st.upper()
x=True




def logic(object):
    point=0
    game=0
    game_dat=["ROCK","PAPER","SCISSOR"]
    item = random.choice(game_dat)
    print(item)
    if object.upper() == "ROCK" and item == "SCISSOR" :
        print("COmputer :{}".format(item))
        print("You WON!..............")
        point +=1
        game +=1
    elif object.upper() == "SCISSOR" and item == "PAPER":
        print("COmputer :{}".format(item))
        print("You WON!..............")
        point +=1
        game +=1
    elif object.upper() == "PAPER" and item == "ROCK":
        print("COmputer :{}".format(item))
        print("You WON!..............")
        point +=1
        game +=1
    elif object.upper() == "END":
        print("Total Games {} \n Total Wins {}".format(point,game) )
    else:
        print("You lose.....!")
        point +=1
        game +=1  

        print(point)
        print(game)      
    

if game_st =="START":
    while x:
        
        inp = input("Enter(ROCK/PAPER/SCISSOR/END) :")
        logic(inp)
    
        

else:
    exit()