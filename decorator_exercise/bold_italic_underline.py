def print_type(type,text):
    return f"<{type}>{text}</{type}>"
def make_underline(func):
    def wrapper(*args):
        result = func(*args)
        return print_type("u",result)
    return wrapper


def make_bold(func):
    def wrapper(*args):
        result = func(*args)
        return print_type("b", result)

    return wrapper


def make_italic(func):
    def wrapper(*args):
        result = func(*args)
        return print_type("i", result)

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
