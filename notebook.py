while True:
    print(" (1) Read the notebook \n (2) Add note\n (3) Empty the notebook\n (4) Quit\n")
    choice = input("Please select one: ")
    if choice == "1":
        file = open("notebook.txt", "r")
        cont = file.read()
        file.close()
        print()
        print(cont)
    elif choice == "2":
        file = open("notebook.txt", "a")
        nt = input("Write a new note: ")
        file.write(nt)
        file.write("\n")
        file.close()
    elif choice == "3":
        file = open("notebook.txt", "w")
        file.close()
        print("Notes deleted")
    elif choice == "4":
        file.close()
        print("Notebook shutting down, thank you.")
        break