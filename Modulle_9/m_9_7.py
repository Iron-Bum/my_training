def is_prime(func):
    def wrapper(*args):
        num_sum = func(*args)
        is_prime_num = True
        for i in range(num_sum - 2):
            if num_sum % (i + 2) == 0:
                is_prime_num = False
                break
        if not is_prime_num:
            print('Составное')
        else:
            print('Простое')
        return num_sum
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)