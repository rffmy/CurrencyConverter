# read animals.txt
with open('animals.txt', 'r') as file:
    lines = file.readlines()

# https://www.pythonpool.com/python-remove-newline-from-list/
for i, line in enumerate(lines):
    lines[i] = line.rstrip() + ' '

# and write animals_new.txt
with open('animals_new.txt', 'w') as file_new:
    file_new.writelines(lines)
