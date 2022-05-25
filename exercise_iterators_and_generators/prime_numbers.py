def get_primes(ll):
    for num in ll:
        if num > 1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))