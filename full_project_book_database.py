#imports
import csv

#Variables
current_ID = 1

new_additions = []

filename = "library.csv"

fields = ['ID', 'Title', 'Author', 'Genre', 'Year', 'Location']

data = []

#Code
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(dict(row))
if len(data) > 0:
    current_ID = data[:-1].get("ID")
    current_ID = int(current_ID) + 1

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
        new_record = {
            "ID": current_ID,
            "Title": input("What is the title of the book? >"),
            "Author": input("What is the author's first name?  >"),
            "Genre": input("What genre is the book?  >"),
            "Year": input("What year was the book released?  >"),
            "Location": input("Where is the book? > ")
        }
        new_additions.append(new_record)
        current_ID = current_ID + 1
        print("-"*15)
        print("New Record added successfully!")
    elif choice == "2":
        #Display the data
        for item in fields:
            print("%-25s"%item, end='')
        print("\n")
        for row in data:
            for key, val in row.items():
                print("%-25s"%val, end='')
            print("\n")
        for row in new_additions:
            for key, val in row.items():
                print("%-25s"%val, end='')
            print("\n")
    elif choice == "3":
        #Search the data
        search_term = input("What would you like to search for?").lower()
        results = []
        for row in data:
            for key, val in row.items():
                if search_term in val.lower():
                    results.append(row)
        for item in new_additions:
            for key, val in item.items():
                if search_term in val.lower():
                    results.append(item)
        #Display the results
        if len(results) > 0:
            for item in fields:
                print("%-25s"%item, end='')
            print("\n")
            for item in results:
                for key, val in item.items():
                    print("%-25s"%val, end='')
                print("\n")
        else:
            print("Sorry no records found")
    elif choice.lower() == "x":
        print("Thank you! Shutting down.")
    else:
        print("Sorry, I didnt recognise that option")
        
if len(new_additions) > 0:
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for item in new_additions:
            writer.writerow(item)
