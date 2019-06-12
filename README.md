# python-database-project

Do you ever feel un-organised? Life can get complicated and there is so much to keep track of, the raw data required can be overwhelming. How can we use computing to solve this problem? If only there was a way of organising and accessing data that would let us get it out of our head. Well, I am here to tell you, there is! Databases are a way of organising the data we care about, so that we can easily access it and use it to make our lives easier.

In this lesson, we are going to create a database, using python and a text file. The example I will be using is a personal library application. I have a lot of books at home, and having a system where I can check which books I have and where they are would be very useful. I have also run this lesson and allowed the students pick their own item to keep track of, it just involves a little more planning time at the end.

To start with, we should look at some key terminology for databases, so that we understand what we are creating in our python code.
 
Databases are organised collections of **data**, this allows them to be displayed, maintained and searched easily. Our database will have 1 **table**, effectively just like a spreadsheet table. The headings on each of the columns are the **fields**, the individual pieces of data we want to store about the books in our collection. The information about a single book are called its **attributes** and are stored toegther in one **record**, which would be a single row in our database table. To make it easier to search and sort our database, we should also select a **primary key**, one field that will be unique for each book. Sometimes one of the fields we are already storing works for this purpose, if not then the database will create an ID number that it uses to uniquely identify each record.

## Design our first record. 

Pull the class back together, ask a few groups about the data they selected to track. Make sure they have chosen appropriate data types. Ask some if they can find any of the fields that would be a primary key, the answer will most likely be no. The ISBN could work, but for our simple application having to type in a 10 or 13 digit number just to use for an ID would be overkill. In our database we are going to generate our own IDs. 

The requirements for our database are that it can do the following things; Save data to a file, read data from that file, create new books, display our full database, allow the user to enter a search term and display a list of relevant results based on that term.

We can decompose the problem into the following steps:
1.	Set up our structures
2.	Create a record
3.	Save the data to the database file
4.	Read from the database file
5.	Display the database to the user
6.	Allow the user to search the database
7.	Display the results

Have the class log in and power up Python, you can complete this activity on a local version, or through trinket.io. If they are doing it locally, have them create a new folder to hold this project, we will be interacting with external files and so having them in the same folder avoids confusion with file locations and paths. They should then load up a new python file.

## Setting up our structures

To start, download the [starter file](https://github.com/m-bowley/python-database-project/blob/master/starter_file_book_database.py) provided. Each student should make a copy of this. 

![Image](/Images/Structures.png)

At first, I have them examine the code, and then get them to run it. Use PRIMM, and get them to print certain messages when a menu option is selected. This can be a great exemplar for making a menu in any application they are developing. 

This will be the skeleton of our database app, giving them a starter file can help ease some cognitive load from students.

Have them examine the variables and make guesses about what they are used for. 
|Variable|Purpose|
|--------|-------|
|*current_ID*|a variable to count up as we create records, this will be our primary key|   
|*new_additions*|a list to hold any new records we make while our code is running, before we save them to the file|
|*filename*|the name of the database file we will be using|
|*fields*|a list of our fields, so that our dictionaries can be aligned with our text file|
|*data*|a list that will hold ALL of the data from the database, so that we can search and display it without having to read the file every time.|
 
## Create our first record

We are going to use dictionaries to store our records. They reference their elements using keys instead of indexes, which fit our database fields nicely. We are going to generate our own IDs. Each of these must be unique, so a variable is needed that we can add to as we make our records. This is a user focussed application so let’s make it so our user can input the data for the first book. The strings, in quotes, on the right of the colon are the keys (the names of our fields) and the data on the right is the stored value, in our case whatever the user inputs in response to our appropriate prompts.

![Image](/Images/FirstRecord.png)

We finish this part of by adding the record to the file, incrementing the current Id and then displaying a useful feedback message to the user to say their record has been created successfully. 

*Save your code, and run it. Make sure there aren’t any syntax errors* 

## Saving it to a text file

Now that we have our first record created. The next step is to save our database to a text file so that we can recall that data whenever we run our program. We are going to do this at the very end of our file.

![Image](/Images/SaveToFile.png)

To do this we will use the csv module. We want to save our data to the text file, as if it was a table. So each line will be a comma separated list of the values in one of our book records. Apart from the first line in the file, which will contain our field labels. There is a special file type for this, called CSV (comma separated values), that can be read using Word or Excel (and equivalents). 

Then we check there is something in the new_additions list, this is for later when it will be possible to run your program without adding a book. We then open the csv file, by calling the open function with the filename variable we set up a moment ago. The second argument is a character, and this is to choose which mode to open in. There are 3 main modes for interacting with files; read, write and append. We want to append as any new data should go on to the end of the file. Append means ‘add at the end’, just like an appendix goes at the end of a book. We then make a csv writer, in this case one that specifically works with dictionaries. The CSV writer does things like adds commas and matches the fields to the dictionary keys. To be able to do this, it needs to know what file it is using, and also what fields it has. We then iterate over our new additions list and write each new item to our database file. The writer does all the finnicky parts, we just hand it a dictionary and it will create a row for us. 

*Save your code, and run it. Make sure there aren’t any errors before continuing* 

You should see that a new file has appeared in your folder, called library.csv (or whichever name you picked). Open it up using excel or word and see what it looks like!

## Read from the database file

Our file should now have at least 1 book in it, but I quite like letting the class add a few more to get comfortable with the program and how it works. So there should be a few more. 

Next you can add the code with them to read from the database file and display the data to the user. 

![Image](/Images/ReadFromFile.png)

Just like the DictWriter we used earlier, there is a DictReader that will do the same thing but in reverse. It will take the comma seperated line and produce a dictionary for us. Then we need to make sure our current_ID is the one after the last line of our database (remember, we don’t want duplicates)

![Image](/Images/DisplayTheData.png)

Next we can add the code to the display the data option in our if statements. We need to display the fields first, then the data from our database file and finally any new additions that have been made since the program has been running. There are 2 oddities in what we do to display the data, one is that because all of our data is stored in dictionaries, we need to print the value and not the key. Also we want to add space to our outputs so that it aligns like a table. 

## Allow the user to search the database

The last bit of essential functionality required for our database is to allow the user to search it. There is lots of room for differentiation here, you can set some to the task of allowing users to search by certain fields, to challenge more competent students, or implement the more simple search done in this code. Using a new array to store any results, we search through both the data from the file and any new additions that have been made since our program started and if the search string is found anywhere in the values of that dictionary, it will be added to our results.

![Image](/Images/SearchTheData.png)

Once the search is complete, if there are any results the fields are printed as table headers and then the results are printed one by one. If there are none, we print a message to the users to let them no their search did not get any hits. 

![Image](/Images/DisplayTheResults.png)

## Wrap Up

This piece of code can be used in your classroom in any way that fits your students. You may want to use PRIMM and give them the [entire code](https://github.com/m-bowley/python-database-project/blob/master/full_project_book_database.py). They can investigate and modify it to their own purpose. You can also lead them through it, having them follow you as you demonstrate how an expert constructs a piece of software. I have done both to great effect, let me know how your classes get on.  
