file = open("strings.txt", "r")
lines = file.readlines()
for line in lines:
    if line.strip().isalnum():
        print (line[:-1] + " was ok.")
    else:
    	print (line[:-1] + " was invalid.")
file.close()