calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_tuple = len(string), string.upper(), string.lower()
    return string_tuple


def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in str(list_to_search).lower():
        return True
    else:
        return False

print(string_info('Urban'))
print(string_info('Student'))
print(is_contains('ban', ['Urban', 'banan', 'bank']))
print(is_contains('cat', ['apple', 'dog', 'juice']))
print(calls)