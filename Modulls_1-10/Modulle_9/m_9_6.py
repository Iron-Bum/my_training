def all_variants(text):
    length = len(text)
    for i in range(length):
        for j in range(length - i):
            i += 1
            yield text[j: i]


a = all_variants('abc')
for k in a:
    print(k)


