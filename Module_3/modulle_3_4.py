def single_root_words(root_words, *other_words):
    same_words = []
    for i in other_words:
        if root_words.lower() in i.lower() or i.lower() in root_words.lower():
            same_words.append(i)
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')