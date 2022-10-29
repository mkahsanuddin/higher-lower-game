import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)


def choice():
    return random.choice(data)


def prepare_choice(computer_cho):
    values = []
    for k, v in computer_cho.items():
        if k != "follower_count":
            values.append(v)

    a_msg = (f"{values[0]}, a {values[1]}, from {values[2]}.")
    return a_msg


computer_choice = choice()

a_short_msg = "Compare A:"
b_short_msg = "Against B:"

a_msg = f"{a_short_msg} {prepare_choice(computer_choice)}"
print(a_msg)
a_follower = computer_choice["follower_count"]
print(a_follower)

print(vs)

vs_matched = True
while vs_matched:
    computer_choice = choice()
    b_follower = computer_choice["follower_count"]
    if a_follower == b_follower:
        continue
    else:
        vs_matched = False

b_msg = f"{b_short_msg} {prepare_choice(computer_choice)}"
print(b_msg)
b_follower = computer_choice["follower_count"]
print(b_follower)

score = 0

game_restart = True

while game_restart:

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (a_follower > b_follower and guess == "a") or (a_follower < b_follower
                                                      and guess == "b"):
        clear()
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")
        if a_follower < b_follower:
            a_msg = f"{a_short_msg} {prepare_choice(computer_choice)}"
            a_follower = b_follower
            print(a_msg)
            print(a_follower)
        else:
            print(a_msg)
            print(a_follower)

        print(vs)

        vs_matched = True
        while vs_matched:
            computer_choice = choice()
            b_follower = computer_choice["follower_count"]
            if a_follower == b_follower:
                continue
            else:
                vs_matched = False

        b_msg = f"{b_short_msg} {prepare_choice(computer_choice)}"
        print(b_msg)
        b_follower = computer_choice["follower_count"]
        print(b_follower)

    else:
        print(b_follower)
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
