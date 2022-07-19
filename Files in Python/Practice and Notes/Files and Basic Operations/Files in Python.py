#We are accessing the file, to read and write data from it.
"""
We are now going to use the open('filename', 'option')
Option includes read(r)

FILE POINTER: We always cannot keep a lot of files open, this will consume RAM and CPU usage.
So to avoid this, we are using a file pointer, which is basically a variable assigned to a file.
my_file = open('filename', 'r')
r here stands for read.
"""

#READING FILES:
my_file = open('data.txt', 'r') #r stands for read.
file_content = my_file.read()
my_file.close()
#We always should close the files after usage, or else the OS will have the file open in background.
print(file_content)


#WRITING FILES:
#Now lets try to write files.

test_file = open('data.txt', 'w')
#Writing the file will overwrite the file and always erase the contents which had been written before.
test_file.write("The world will gradually become a better place to live!!")
test_file.close()


"""
USER INPUT AND WRITING INTO FILE.
"""

name = input("Enter your name: ")
#Here we should not open the file before getting the user input, which will increase the CPU and Memory usage.
#So we should ensure the file is open for the shortest period of time possible.
input_test = open('data.txt', 'w')
input_test.write(name)
input_test.close()
