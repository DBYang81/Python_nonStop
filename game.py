import random

list = ["Foot", "Nuke", "Cockroach"]


def randres():
    rob = random.randint(1, 3)
    if rob == 1:
        return "Foot"
    elif rob == 2:
        return "Nuke"
    else:
        return "Cockroach"

def tester(input_data, computer_choice):
    if input_data == "Foot":
        if computer_choice == "Foot":
            print("It is a tie!")
            return "tie"
        elif computer_choice == "Nuke":
            print("You Lose!")
            return "lose"
        elif computer_choice == "Cockroach":
            print("You Won!")
            return "win"
    if input_data == "Nuke":
        if computer_choice == "Foot":
            print("You Won!")
            return "win"
        elif computer_choice == "Nuke":
            print("You Both Lose!")
            return "lose"
        elif computer_choice == "Cockroach":
            print("You Lose!")
            return "lose"
    if input_data == "Cockroach":
        if computer_choice == "Foot":
            print("You Lose!")
            return "lose"
        elif computer_choice == "Nuke":
            print("You Won!")
            return "win"
        elif computer_choice == "Cockroach":
            print("It is a tie!")
            return "tie"

def main():
    sum = 0
    tie = 0
    win = 0
    while True:
        input_data = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if input_data == "Quit":
            print("You play ", sum, " rounds, and won ", win, " rounds, playing tie in ", tie, "rounds.")
            exit()
        if input_data in list:
            sum += 1
            print("You chose: ", input_data)
            computer_choice = randres ()
            print("Computer chose: ", computer_choice)
            what = tester(input_data, computer_choice)
            if what == "win":
                win += 1
            elif what == "tie":
                tie += 1
        else:
             print("Incorrect selection.")

if __name__ == "__main__":
    main()
    