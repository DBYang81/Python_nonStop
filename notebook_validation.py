import time

def filechecker(filename):
    try:
        file = open(filename, "r")
    except IOError:
        if filename == "notebook.txt":
            print("No default notebook was found, created one.")
        else:
            print("No notebook with that name detected, created one.")
        file = open(filename, "w")
        file.close()
        print("Now using file " + filename)
    else:
        print("Now using file " + filename)
        file.close()
    return filename
        
def main():
    ret = filechecker("notebook.txt")

    while True:
        print(" (1) Read the notebook\n (2) Add note\n (3) Empty the notebook\n (4) Change the notebook\n (5) Quit\n")
        choice = input("Please select one: ")
        if choice == "1":
            file = open(ret, "r")
            cont = file.read()
            file.close()
            print(cont)
            print()
            print("Now using file " + ret)
        elif choice == "2":
            file = open(ret, "a")
            nt = input("Write a new note: ")
            print("now using file " + ret)
            file.write(nt + ":::" + time.strftime("%X %x") + "\n")
            file.close()
        elif choice == "3":
            file = open(ret, "w")
            file.close()
            print("Notes deleted")
        elif choice == "4":
            newfile = input("Give the name of the new file: ")
            ret = filechecker(newfile)
        elif choice == "5":
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()