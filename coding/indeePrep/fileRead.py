"""
read(): Returns the read bytes in form of a string. Reads n bytes,
        if no n specified, reads the entire file.
        File_object.read([n])

readline(): Reads a line of the file and returns in form of a string.
        For specified n, reads at most n bytes. However, does not reads more than one line,
        even if n exceeds the length of the line.
        File_object.readline([n])

readlines(): Reads all the lines and return them as each line a string element in a list.
        File_object.readlines()
Note: ‘\n’ is treated as a special character of two bytes.


"""
import csv
import json

with open('file.txt') as f:
    text = f.read()
    print(text)

# Python code to illustrate split() function
with open('file.txt') as f:
    text = f.readlines()
    for line in text:
        print(line.split())
# ['overriding', 'existing', 'text']
# ['appending', 'to', 'existing', 'text']

with open('file.txt', 'w') as f:
    f.write("overriding existing text")

with open('file.txt','a') as f:
    f.write('\nappending to existing text')

# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print(file.read(5))  # overr

print('-------------------------------')
import os


def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)


def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)



# CSV
with open('test.csv', mode='w', newline="") as file:
    csv_content = csv.writer(file)
    csv_content.writerow(['Name','Angel'])
    csv_content.writerow(['Name','Bailey'])

with open('test.csv', mode='r') as file:
    csv_read = csv.reader(file)
    print(csv_read)
    for i in csv_read:
        print(i)

# fields = csvreader.next()
# csvreader is an iterable object. Hence, .next() method returns the current row and
# advances the iterator to the next row. Since, the first row of our csv file contains
# the headers (or field names), we save them in a list called field
# json
with open('data.json', 'w') as file:
    content = {
        'name':'ram',
        'role':'king'
    }
    json.dump(content, file)


with open('data.json') as file:
    data = json.load(file)
    print(data)


"""
24. Explain the concept of context managers in Python.

Provide safe and efficient handling of resources like files, databases, or network connections.
Use the with statement to automatically perform resource allocation upon entering the block and deallocation upon exiting, even if exceptions occur.
Ensures resources are properly closed and prevents leaks.
"""



