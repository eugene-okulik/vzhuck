s = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
     Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = s.split()
punctuation = '.,?!'
new_list = []
for word in words:
    if word[-1] in punctuation:
        new_word = word[:-1] + "ing" + word[-1]
    elif word[-1] not in punctuation:
        new_word = word + "ing"
    new_list.append(new_word)
result = ' '.join(new_list)
print(result)
