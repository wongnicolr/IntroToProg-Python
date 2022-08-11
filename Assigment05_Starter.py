# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Nicole Wong, 09Aug2022, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
dic1 = {"task": "homework", "priority":"1"}
dic2 = {"task": "laundry", "priority":"3"}
dic3 = {"task": "work out", "priority":"2"}
objFile = open(strFile, "w")
objFile.write(dic1["task"]+ ","+ dic1["priority"] + "\n")
objFile.write(dic2["task"]+ ","+ dic2["priority"] + "\n")
objFile.write(dic3["task"]+ ","+ dic3["priority"] + "\n")
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        print("TASK      | PRIORITY")
        for row in objFile:
            lst = row.split(",")
            print(lst[0] + ' | ' + lst[1].strip())
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        t = input("Add a new task: ")
        p = input("List the priority of task: ")
        objFile = open(strFile, "a")
        objFile.write(t + "," + p + "\n")
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        import os
        with open("ToDoList.txt", "r") as inpu:
            with open("other.txt", "w") as output:
                for line in inpu:
                    x = input("Hit enter to remove a task: ")
                    if not line.strip("\n").startswith(x):
                        output.write(line)
        os.replace("other.txt", "ToDoList.txt")
        objFile.close()
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Data saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Hit enter to exit")
        break  # and Exit the program
