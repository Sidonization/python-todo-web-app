FILEPATH = "todos.txt"


def get_todos(filepath_arg=FILEPATH):
    """ Read the list of todos from a text file """
    with open(filepath_arg, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def set_todos(todos_arg, filepath_arg=FILEPATH):
    """ Write the list of todos to a text file """
    with open(filepath_arg, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
