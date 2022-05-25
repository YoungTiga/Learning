def print_row(size, star_count):

    for row in range(size-star_count):

        print(" ", end="")

    for row in range(1, star_count):
        print("*", end=" ")

    print("*")
def print_upper(n):
    for star_count in range(1, n):
        print_row(n, star_count)
def print_lower(n):
    for star_count in range(n, 0, -1):
        print_row(size, star_count)

size = int(input())

print_upper(size)
print_lower(size)
