# Functions library
FILEPATH = "todos.txt"

def get_todos():
    with open('todos.txt', 'r') as file:
        todos = list(file)
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def append_todo(todos_arg, filepath=FILEPATH):
    with open(filepath, 'a') as file:
        file.writelines(todos_arg + "\n")