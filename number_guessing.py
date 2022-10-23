import random
# play against a random number generated by a computer.
# Implement a feature to count number of times number has been 
# attempted, and output the value once the correct guess has been
# made.
def guess_number():
    num=random.randint(1,100)
    while True:
        my_guess=int(input("Number to guess:"))
        if num==my_guess:
            print("You won")
            break
        elif my_guess>num:
            print("Too high, choose a smaller num")
        else:
            print("Too low, choose a bigger num")

# guess_number()
# play_again=input("do you want to play again")
# if play_again=='y':
#     guess_number()
# else:
#     pass

# Computer makes the guess.
def computer_guess():
    h=10
    l=1
    feedback=""
    guess=random.randint(l,h)
    while feedback!='c':
        print(f"is{guess} higher than number to guess?")
        feedback=input().lower()
        if feedback=='l':
             guess=random.randint(guess,h)
        elif feedback=='h':
            guess=random.randint(l,guess)
        else:
            feedback='c'
    print('Computer won!!!!')

computer_guess()


