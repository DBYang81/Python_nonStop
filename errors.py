def main():
    filename = input("Give a file name: ")

    try:
        file = open(filename, "r")
        content = file.read()
        num = int(content)
        result = 1000 / num


    except IOError:
        print("There seems to be no file with that name.")
    except ValueError:
        print("The file contents are unsuitable.")
    except ZeroDivisionError:
        print("There was a problem with the program.")

    else:
        print("The result was ", result)

if __name__ == "__main__":
    main()