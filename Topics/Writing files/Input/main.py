# write the code here
line = input()

with open('input.txt', 'w') as file:
    file.write(line)
    file.close()
