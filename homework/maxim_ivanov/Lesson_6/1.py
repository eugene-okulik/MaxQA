# Задание №1
text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

new_text_list = []
text_split = text.split()

for word in text_split:
    if ',' in word:
        new_word = word.replace(',', '')
        new_text_list.append(new_word + 'ing' + ',')
    elif '.' in word:
        new_word = word.replace('.', '')
        new_text_list.append(new_word + 'ing' + '.')
    else:
        new_text_list.append(word + 'ing')
print(' '.join(new_text_list))
