import random


user_wins=0
computer_wins=0

while True:
    user_input=input("\nEnter your choice: rock, paper or scissor? OR Q TO QUIT\n").lower()
    if user_input=='q':
        break
    if user_input not in ['rock','paper','scissor']:
        print("Invalid input, please enter again")
        continue
    random_num=random.randint(0,2)
    # rock:0, paper:1, scissor:2
    computer_input=['rock','paper','scissor'][random_num] 
    print("Computer chose:",computer_input+".")

    if user_input==computer_input:
        print("It's a tie!")
    elif user_input=='rock' and computer_input=='scissor':
        print("You won!")
        user_wins+=1
    elif user_input=='paper' and computer_input=='rock':
        print("You won!")
        user_wins+=1
    elif user_input=='scissor' and computer_input=='paper':     
        print("You won!")
        user_wins+=1
    else:
        print("You lost!")
        computer_wins+=1
print("You won",user_wins,"times.")
print("Computer won",computer_wins,"times.")
print("Goodbye!")  


