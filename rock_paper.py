import random
# An improvement to be made here is regarding validation \
# of user input.
# also add the feature for a tie, ie similar choice

def Rock_Paper_Scissors(my_list=['r','p','s']):
    print('Let us play rock paper scissors!!!')
    won=False
    while not won:
        player=input("Rock (r), Paper(p) or Scissors(s)").lower()
        opponent=random.choice(my_list)
        if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') \
            or (player=='p' and opponent=='r'):
            print("You Won!")
            won=True
            return 
            # break
        else:
            print('Computer Won!!')
            won=True
            return
            # break

Rock_Paper_Scissors()
play_again=input("Play again? y/n").lower()
if play_again=='y':
    Rock_Paper_Scissors()


      
