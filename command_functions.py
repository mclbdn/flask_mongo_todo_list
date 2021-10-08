from TodoItem import TodoItem

# Add an Item To The List
def addTodoItem(col, user_input):
    item = TodoItem()
    item.todo_name = user_input
    col.insert_one({"todo_name": item.todo_name, "_id": item._id})

# Fulltext Search In A Collection
def searchItem(col, user_input):
    if len(list(col.find( { "$text": { "$search": user_input } } ))) != 0:
        cursor = []
        for result in col.find( { "$text": { "$search": user_input } } ):
                cursor.append(result)
    else:
        return None
    return cursor

# Does ID Exist In A Collection?
def id_exists(col, todo_id):
    if len(list(col.find({"_id": todo_id}))) != 0:
            return True
    return False

# Edit A Single Item
def editTodoItem(col, todo_id, new_text):
    if id_exists(col, todo_id):
        col.update_one({"_id": todo_id}, {"$set": {"todo_name": new_text}})
        return True


# Delete A Single Item
def deleteTodoItem(col, user_input):
    if id_exists(col, user_input):
        col.delete_one({"_id": user_input})
        return True
