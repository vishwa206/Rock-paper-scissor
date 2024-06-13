import random
option=("rock","scissor","paper")
computer_turn = random.choice(option)
user_turn = input("select rock/paper/scissor:").lower()
print("computer choice:",computer_turn)

if (user_turn==computer_turn):
    print("Tie")
elif (user_turn=="rock" ):
    if computer_turn=="scissor":
        print("user wins")
    elif (computer_turn=="paper"):
        print("computer wins")
elif(user_turn=="scissor"):
    if(computer_turn=="paper"):
        print("user wins")
    elif (computer_turn=="rock"):
        print("computer wins")
elif(user_turn=="paper"):
    if(computer_turn=="rock"):
        print("user wins")
    elif(computer_turn=="scissors"):
        print("computer wins")
   
    




