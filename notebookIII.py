import time
import pickle

def notechecker():
    try:
        file = open("notebook.dat", "rb")
    except IOError:
        print("No default notebook was found, created one.")
        file = open("notebook.dat", "wb")
        file.close()
    else:
        file.close()

def main():
    notechecker()
    list = []

    while True:

        print(" (1) Read the notebook\n (2) Add note\n (3) Edit a note\n (4) Delete  a note\n (5) Save and Quit\n ")
        
        ch = input("Please select one: ")
        if ch == "1":
            try:
                list = pickle.load(open("notebook.dat", "rb")) 
                #pickle.load or dump(open(filename, mode)) not require close file
            except EOFError:
                print()
            else:
                for word in list:
                    print(word)
        elif ch == "2":
            newinput = input("Write a new note: ")
            newnote = newinput + ":::" + time.strftime("%X %x") + "\n"
            list.append(newnote)
            pickle.dump(list, open("notebook.dat", "wb"))
        elif ch == "3":
            if len(list) > 0:
                print("The list has", len(list), "notes.")
                num = int(input("Which of them will be changed?: "))
                print(list[num])
                changedNote = input("Give the new note: ")
                list[num] = changedNote + ":::" + time.strftime("%X %x")
                pickle.dump(list, open("notebook.dat", "wb"))               
        elif ch == "4":
            if len(list) > 0:
                print("The list has", len(list), "notes.")
                deleted = int(input("Which of them will be deleted?: "))
                if deleted - 1 < len(list):
                    print("Deleted note " + list[deleted - 1])
                    list.pop(deleted - 1)
                    pickle.dump(list,open("notebook.dat", "wb"))
                else:
                    print("Wrong one!")
        elif ch == "5":
            pickle.dump(list, open("notebook.dat", "wb"))
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()