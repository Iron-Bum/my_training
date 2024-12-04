def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'a', encoding='UTF-8') as file:
        num_str = 0
        for i in strings:
            num_str += 1
            strings_positions[(num_str, file.tell())] = i
            file.write(f'{i}\n')
        return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
