with open('randomtxt.txt') as file:
    lines = file.readlines()
    append_words = 'mytext'
    appended_lines = [line.strip() + append_words + '\n' for line in lines]


with open('result.txt', 'w') as fole:
    fole.writelines(appended_lines)

print("appending successfull!")