##This is a game about ston ,paper and Scissor
import random

user_score=0
pc_score=0

myList=['r','p','s']


def take_input():
    print("1.Rock (r) \n 2.Papper (p) \n 3.Scissor (s)")
    user_choice=input("Enter Your choice :")

    while user_choice not in myList:
        print("Wrong Input!")
        user_choice=input("Enter Your choice :")
    
    return user_choice


def clash(a,b):

    if {a,b} == {'r','p'}:
        return 'p'
    elif {a,b} == {'r','s'}:
        return 'r' 
    else:
        return 's'
    
print("Welcome to my Game!!!")

while(user_score  < 3 and pc_score < 3):
    user_choice=take_input()
    pc_choice=random.choice(myList)

    if user_choice == pc_choice :
        print(f"Computer choice is {pc_choice}")
        print(f"TIE!")
        input()

    elif user_choice == clash(user_choice,pc_choice):
        user_score += 1
        print(f"Computer choice is {pc_choice}")
        print("You Won!!! :)")   
        input()

    else:
        pc_score += 1
        print(f"Computer choice is {pc_choice}")
        print("You loose :(")
        input()


if(user_score > pc_score):
    print("EXECELLENT!! YOU WON!!")
else:
    print("YOU LOST!")





