## rock paper scissor
import random

user_action =input("enter rock,scissor,paper: ")
possible_action = ["rock", "paper","scissor"]
opponenet_action = random.choice(possible_action)
print(f"\n you choose {user_action}, computer choose {opponenet_action}.\n")

if user_action == opponenet_action:
    print("both player choose {user_action}\n")
elif user_action == "rock":
    if opponenet_action == "scissor":
        print(f"\nyou have choosen {user_action} you won.\n")
    else:
        print(f"\nyou have choosen {user_action} you loose.\n")
elif user_action == "paper":
    if opponenet_action == "rock":
        print(f"\nyou have choosen {user_action} you win.\n")
    else :
        print(f"\nyou have choosen {user_action} you loose.\n")
elif user_action == "scissor":
    if opponenet_action == "rock":
        print(f"\nyou have choosen {user_action} you loose.\n")
    else :
        print(f"\nyou have choosen {user_action} you win.\n")
