#imports
import csv

#Variables
current_ID = 1

new_additions = []

filename = "library.csv"

fields = ['ID', 'Title', 'Author', 'Genre', 'Year', 'Location']

data = []

#Code

print("------Welcome to the Python Library organiser------")

choice = ""

while choice.lower() != "x":
    print("""What would you like to do?
    1 - Add a book
    2 - Display your Books
    3 - Search for a Book""")

    choice = input(">")

    if choice == "1":
        #Code to add a record
        
    elif choice == "2":
        #Display the data
        
    elif choice == "3":
        #Search the data
       
        #Display the results
        
    elif choice.lower() == "x":
        print("Thank you! Shutting down.")
    else:
        print("Sorry, I didnt recognise that option")
        

