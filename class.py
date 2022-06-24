class Player:
    teamcolor = ""
    points = 0

def main():
    david = Player()
    david.teamcolor = "Blue"
    david.points = 300
    print(f"The {david.teamcolor} contender has {david.points} points!")

if __name__ == "__main__":
    main()


