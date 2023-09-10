import os
import random
import art
from game_data import data


# initiate score for game
score = 0

def clear():
    os.system('clear')

# generate two persons for comparison
# and ensure 2nd one is not the same as 1st one
def generate_person1():
    return random.choice(data)
person1 = generate_person1()

def generate_person2():
    person2 = random.choice(data)
    # make sure we do not compare the same person
    while person2 == person1:
        person2 = random.choice(data)
    return person2
person2 = generate_person2()

# print the names of persons to be compared
def get_full_information(person):
    return f"{person['name']}, {person['description']} from {person['country']} "

def get_followers_amount(person):
    return int(person['follower_count'])

# compare two generated persons' amount of followers
def compare_followers(person1, person2):
    if get_followers_amount(person1) > get_followers_amount(person2):
        return 1
    else:
        return 2

# BEGINNING OF THE GAME
print(art.logo)

game_on = True

while game_on:
    print(art.one + get_full_information(person1))
    print(art.divider)
    print(art.two + get_full_information(person2))
    # compare two generated persons' amount of followers
    # and save to actual_result
    actual_result = compare_followers(person1, person2)

    actual_person = 0
    if actual_result == 1:
        actual_person = person1
    else:
        actual_person = person2

    # make a guess, 1st or 2nd
    guess = int(input(f'\nPlease make a guess who has higher amount of followers in the Instagram between two of these. Type 1 or 2: '))

    # compare actual_result and guess
    # if equal -> add 1 point to score, assign person2 to person1 and generate new person2,
    # and repeat the game starting from comparison of 2 generated persons
    # if not equal -> show: actual_result, final score and goodbye message
    if actual_result == guess:
        score += 1
        person1 = actual_person
        person2 = generate_person2()
        print(f'\nGuess is right, your score is {score}. ')
    else: 
        game_on = False
        print(f'\nSorry, that\'s wrong, {actual_person["name"]} has more followers.')
        print(f'Your final score is {score}. ')
