# Задание №2
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_key(words):
    for key, value in words.items():
        j = 0
        final_str = ''
        while j < value:
            final_str = final_str + key
            j += 1
        print(final_str)


print_key(words)
