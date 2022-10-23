from words import words
import random
import string

def get_valid_word(words):
    word=random.choice(words).upper()
    print(word)
    while '-' in word or ' ' in word:
        word=random.choice(words).upper()
    return word

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    end=True
    while len(word_letters)>0 and lives>0:
        print("You have used these letters: " ''.join(used_letters))
        # Tell suer what current word is:
        #  we use list comprehension here below
        word_list=[letter if letter in used_letters else'-' for letter in word]
        print(word_list)
        user_letter=input("Guess letter in word: ").upper()
        if user_letter in alphabet-used_letters:
              used_letters.add(user_letter)
              if user_letter in word_letters:
                     word_letters.remove(user_letter)                     
        elif user_letter in used_letters:
            print("already guessed the letter")
        elif user_letter !=word_letters:
            lives-=1
        else:
            print("wrong character guessed")
    return word
    
x=hangman()

print("Congrats: the word is: " + ''.join(x))
