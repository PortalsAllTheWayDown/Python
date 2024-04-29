# Python Interacting with files

myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('Goodby text file\n')
myfile.close()

#if the file doesnt exist it will create the file.
#you can also read the file

# Open the file in read mode
with open('myfile.txt', 'r') as file:
    # Read the entire contents of the file
    contents = file.read()
    # Print the contents
    print(contents)