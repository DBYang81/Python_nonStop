class Player:
    teamcolor = ""
    __points = 0

    def tellscore(self):
        print(f"I am {self.teamcolor}, we have {self.__points} points!")

    def goal(self, value = 1):
        self.__points += value



def main():
    david = Player()
    david.teamcolor = 'Blue'
    david.goal() 
    david.tellscore()

if __name__ == "__main__":
    main()