import functions

def check(command_type):
    if command_type == "__VERSION__":
        return print(functions.get_version())