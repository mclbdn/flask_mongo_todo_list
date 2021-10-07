from TodoItem import TodoItem

# Add an Item To The List
def addTodoItem(col, user_input):
    # todo_name = input("Enter a todo name: ")
    print("Called")
    item = TodoItem()
    item.todo_name = user_input
    col.insert_one({"todo_name": item.todo_name, "_id": item._id})
    print("Todo successfully added.")

# Fulltext Search In A Collection
def searchItem(col, user_input):
    print(col)
    print(user_input)
    if len(list(col.find( { "$text": { "$search": user_input } } ))) != 0:
        print("Inside")
        for result in col.find( { "$text": { "$search": user_input } } ):
                print(result)
    else:
        print("No result found")

# Does ID Exist In A Collection?
def id_exists(col, todo_id):
    if len(list(col.find({"_id": todo_id}))) != 0:
            print("ID successfully found.")
            return True
    print("No ID found.")
    return False

# Edit A Single Item
def editTodoItem(col):
    todo_id = input("Enter a valid todo ID to edit: ")
    if id_exists(col, todo_id):
        col.update_one({"_id": todo_id}, {"$set": {"todo_name": input("Enter a new todo text: ")}})
        print("Todo text successfully updated.")


# Delete A Single Item
def deleteTodoItem(col, user_input):
    if id_exists(col, user_input):
        col.delete_one({"_id": user_input})
        print("Todo item successfully deleted.")
