# slang
Documentacion 
    Importing Modules:
        The sqlite3 module is imported to handle SQLite database operations.

    Class Slang:
        This class represents a slang word along with its meaning. It has an __init__ method to initialize the word and meaning attributes.

    Output Formatting:
        Several string constants are defined to help format output strings.

    Connecting to the Database:
        The code establishes a connection to a SQLite database named "slang.db" and creates a cursor to execute SQL queries.

    Creating Table:
        An attempt is made to create a table named "SlangPanameno" in the database to store slang words and meanings. If the table already exists, the code continues without an error.

    SQL Statements:
        A set of functions is defined to perform various database operations using SQL statements. These include inserting records, editing records, deleting records, retrieving all records, and searching for a specific word's meaning.

    Program Functions:
        Additional functions are defined to provide the functionality of the program. These functions include:
            add_word: Allows the user to add a new slang word and its meaning to the database.
            edit_word: Lets the user edit an existing slang word's details.
            del_word: Enables the user to delete a slang word from the database.
            see_words: Displays all the slang words and their meanings stored in the database.
            get_meaning: Allows the user to search for the meaning of a specific slang word.

    Program Loop:
        The main loop of the program runs continuously until the user decides to exit. It presents a menu of options to the user and processes their choice using the new Python 3.10 match statement. The available options are:
            Adding a new word.
            Editing an existing word.
            Deleting a word.
            Viewing all words.
            Searching for a word's meaning.
            Exiting the program.

    Closing Connection:
        Once the loop ends, the program closes the database connection.

Please note:

    The code expects Python 3.10 for the match statement to work as intended.
    The code should be run in an environment with SQLite support.

This code effectively allows the user to manage a simple dictionary of Panamanian slang words and their meanings through a command-line interface.
