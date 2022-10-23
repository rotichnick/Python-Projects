# name="Nickolas"
# print("My name is: {}".format(name))
# print(f"My name is: {name}")
import random
def adjectives():
    my_adjectives=["Amazing","Wonderful","Joyful","Exciting","refreshing"]
    choose=random.choice(my_adjectives)
    # print(random.random())
    return choose


# adjectives()
# adj=input("Adjective")
verb1=input("First Verb ")
verb2=input("Second Verb")
famous_person=input("Famous Person: ")
madlib=f"Computer programming is soo {adjectives()}! It makes me soo excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are a {famous_person}! "
print(madlib)