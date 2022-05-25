def multiply(times):
    def decorator(function):
        def wrapper(n):
            res = function(n)
            res *= times
            return res
        return wrapper
    return decorator

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
