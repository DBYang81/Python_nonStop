class Player:
    """Player-class: stores data on team colors and points."""
    teamcolor = ""
    __points = 0

    def __init__(self):
        col = input("What color do I get?: ")
        self.teamcolor = col


    def tellscore(self):
        print(f"I am {self.teamcolor}, we have {self.__points} points!")

    def goal(self, value = 1):
        self.__points += value



def main():
    player1 = Player()
    player2 = Player()

    player1.goal()
    player1.goal()
    player1.tellscore()
    
    player2.goal()
    player2.tellscore()

if __name__ == "__main__":
    main()