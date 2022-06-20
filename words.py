words = []
file = open("words.txt", "r")
for i in file:
    words.append(i)
words.sort()
print("Words in alphabetical order: ")
for word in words:
    print(word)
    