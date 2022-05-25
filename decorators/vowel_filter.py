def vowel_filter(function):

    def wrapper():
        ll = function()
        return [x for x in ll if x in "AaEeIiOoUu"]

    return wrapper
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
