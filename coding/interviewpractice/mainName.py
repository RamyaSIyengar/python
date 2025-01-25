
# print(__name__)   # __main__
# The __name__ property displays the name of the present module.
# This property offers different values relying on where we run the Python file.


def main():
    print("something")


if __name__ == '__main__':
    main()

#  if conditional clause to check if the value of the __name__ variable
#  is equal to the __main__, then the main() function will execute.

"""
However, when we execute the file as a module by importing it in the 
python_main.py, the program returns no output as the main() function 
is not called.
Thus, we can conclude the custom main() function we have defined in the
classObjects.py file can only be executed as a standalone script but not 
as an imported module.

This is the standard method to define the main() function explicitly in Python. 
It is among the most popular use cases of the __name__ property of a Python file.
"""


