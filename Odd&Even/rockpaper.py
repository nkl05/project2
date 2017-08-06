player1 = raw_input("enter player1 name :")
player2 = raw_input("enter player2 name :")
choice = "Y"
while(choice != "N"):
    p1 = str(raw_input(player1 +" enter your choice from rock, paper or scissor :"))
    p2 = str(raw_input(player2 +" enter your choice from rock, paper, scissor :"))
    if(str(p1) =="rock" and str(p2) =="paper"):
        print str(player1)+"wins"
    elif(str(p1) == "paper" and str(p2) == "scissor"):
        print str(player2)+ "wins"
    elif(str(p1) == "scissor" and str(p2)+"rock"):
        print str(player2)+"wins"
    elif(str(p1) == "rock" and str(p2) == "scissor"):
        print str(player1)+"wins"
    choice = raw_input("to play more enter Y or N to exit")

