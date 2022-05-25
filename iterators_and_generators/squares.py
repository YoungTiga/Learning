def squares(num):
    n = 1
    while n <= num:
        yield n*n
        n += 1



print(list(squares(5)))