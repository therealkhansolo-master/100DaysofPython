# Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
# It is used for:
# web development(server-side), software development, mathematics, system scripting.

# What can Python do?
# Python can be used on a server to create web applications.
# Python can be used alongside software to create workflows.
# Python can connect to database systems. It can also read and modify files.
# Python can be used to handle big data and perform complex mathematics.
# Python can be used for rapid prototyping, or for production-ready software development.

# Why Python?
# Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
# Python has a simple syntax similar to the English language.
# Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
# Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
# Python can be treated in a procedural way, an object-oriented way or a functional way.

# Good to know
# The most recent major version of Python is Python 3, which we shall be using in this tutorial.
# In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.
# Python Syntax compared to other programming languages
# Python was designed for readability, and has some similarities to the English language with influence from mathematics.
# Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
# Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

#Many Windows PCs and Mac computers already have Python pre-installed.
#To check if Python is installed on Windows, search in the start bar for Python or run the following on the Command Line (cmd.exe):
#C:\Users\Your Name>python --version

#Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.
#Simple as that. Save your file. Open your command line, navigate to the directory where you saved your file, and run:
#C:\Users\Your Name>python hello.py

#To check the Python version of the editor, you can find it by importing the sys module:
##Check the Python version of the editor:
import sys
print(sys.version)

#To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. 
# This is made possible because Python can be run as a command line itself.
#Type the following on the Windows, Mac or Linux command line:
#C:\Users\Your Name>python
#Or, if the "python" command did not work, you can try "py":
#C:\Users\Your Name>py

#From there you can write any python code, including our hello world example from earlier in the tutorial:
#C:\Users\Your Name>python
#Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> print("Hello, World!") #Which will write "Hello, World!" in the command line.

#Whenever you are done in the python command line, you can simply type the following to quit the python command line interface:
#exit()

#Indentation refers to the spaces at the beginning of a code line.

#Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
#Python uses indentation to indicate a block of code.
if 5 > 2:
  print("Five is greater than two!")

#Python will give you an error if you skip the indentation:
#Syntax Error:
# if 5 > 2:
# print("Five is greater than two!")
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
#Syntax Error:
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")
 
#In Python, a variable is created when you assign a value to it:
x = 5
y = "Hello, World!"

#Python has no command for declaring a variable.

#Python has commenting capability for the purpose of in-code documentation.

#Comments start with a #, and Python will render the rest of the line as a comment:
#Comments in Python:
#This very line is a comment.
print("Hello, World!")

#A computer program is a list of "instructions" to be "executed" by a computer.

#In a programming language, these programming instructions are called statements.

#he following statement prints the text "Python is fun!" to the screen:
print("Python is fun!")