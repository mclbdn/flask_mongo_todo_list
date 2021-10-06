import uuid

class TodoItem:
    def __init__(self):
        self.todo_name = ""
        # Create my own ID instead of Mongo's
        self._id = str(uuid.uuid4())[:8]
