def main():
    val = input("Give a number: ")

    try:
        val = int(val)
    except Exception:
        print("The input was malformed.")
    else:
        print("The input was suitable!")

if __name__ == "__main__":
    main()