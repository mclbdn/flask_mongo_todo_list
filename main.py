from pymongo import MongoClient
from command_functions import addTodoItem, editTodoItem, searchItem, deleteTodoItem
import os

# Your credentials from Mongo DB Atlas Database User
USERNAME = os.environ.get("MONGO_DB_USER")
PASSWORD = os.environ.get("MONGO_DB_PASSWORD")

# Mongo Setup
# Create a new database with name "cliTodoListDatabase" in Mongo DB Atlas and access it like bellow
client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.wdagb.mongodb.net/cliTodoListDatabase?retryWrites=true&w=majority")

db = client.get_database("cliTodoListDatabase") 

db_todos_collection = db.get_collection("Todos")

# Setup index for search for todo_name
#db_todos_collection.create_index([('todo_name', 'text')])

print("Welcome to the cli todo list")

app_running = True

while app_running:
    user_input = input("Please enter a valid command or see the list of valid commands by typing '--help': ")

    if user_input.lower() == "add":
        addTodoItem(db_todos_collection)
    elif user_input.lower() == "edit":
        editTodoItem(db_todos_collection)
    elif user_input.lower() == "delete":
        deleteTodoItem(db_todos_collection)
    elif user_input.lower() == "search":
        searchItem(db_todos_collection)
    elif user_input.lower() == "quit":
        print("Goodbye")
        app_running = False
    elif user_input.lower() == "--help":
        print(
            """
    List of commands:

    add       Add an item to the todo list.
    search    Text search for an item in the todo list.
    edit      Edit an item from the todo list.
    delete    Delete an item from the todo list.
    quit      Quit app.
        """
        )
    else:
        print("Invalid command")
