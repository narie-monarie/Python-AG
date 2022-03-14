Lines = ["This is line 1\n",
         "This is line 2\n",
         "This is line 3\n"]

with open("start.txt","w") as file1:
    for line in Lines:
        fileStuff = file1.write(line)
    print(fileStuff)


with open("start.txt","r") as file1:
    fileStuff = file1.read()
    print(fileStuff)

# The most common modes used when opening a file - (a)ppend, (r)ead, (w)rite 
# the data attribute that will return the title of the file - file1.name 