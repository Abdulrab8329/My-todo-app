# todos = [] NOW THIS IS  NOT NEEDED! WE ADDS TXTFILE TO STORE LIST
FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """" Read a text file and returns a list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local
def write_todos(todos_local,filepath=FILEPATH):
    """" Write the to-do items in text file """
    with open(filepath, 'w') as file2:
        file2.writelines(todos_local)


if __name__=="__main__":
    print("Hello")