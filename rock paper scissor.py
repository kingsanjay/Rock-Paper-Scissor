1import random
while True:
    opt=("Rock","Paper","Scissor")
    cmpChoice=random.choice(opt)
    print("Enter your choice\n 1 Rock\n 2 Paper \n 3 Scissor")
    opt2 = {1:"Rock", 2:"Paper", 3:"Scissor"}
    i=int(input())
    if i>3:
        print("Invalid Input, \nPlease Enter Correct choice\n\n")
        continue;
    print("Your choice is "+opt2[i])
    print("Computer Choose "+cmpChoice)
    if cmpChoice == opt2[i]:
        print("Game tie")
    elif (cmpChoice == "Rock"and opt2[i]=="Scissor"):
        print("Sorry!!! You loose")
    elif (cmpChoice =="Rock" and opt2[i]=="Paper"):
        print("Congratulation!!! You Won")
    elif (cmpChoice =="Paper" and opt2[i]=="Scissor"):
        print("Congratulation!!! You Won")
    elif (cmpChoice =="Paper" and opt2[i]=="Rock"):
        print("Sorry!!! You Loose")
    elif (cmpChoice == "Scissor" and opt2[i] == "Paper"):
        print("Sorry!!! You Loose")
    elif (cmpChoice == "Scissor" and opt2[i] == "Rock"):
        print("Congratulation!!! You Won")
    a=input("Would You like to continue (y/n)\n")
    if (a=="y" or a=="Y"):
        continue;
    else:
        if (a=="n" or a== "N"):
            break;
        else:
            print("Invalid Input")
            break;