#documentation strings / docstrings

greet = 1
def greet(name):
    """ This function takes a name as an argument and returns a grreting message.

    Parameters:
    name (str) : The name of the person to greet

    Return:
    str: A greeting message

    """
    return f"Hello,{name}!"

print(greet("Rhea"))
