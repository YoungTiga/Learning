def cache(func):
    log = {}
    def wrapper(num):
        if num not in log:
            res = func(num)
            log[num] = res
            return res
        wrapper.log = log
        return log[num]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(3)
print(fibonacci.log)
