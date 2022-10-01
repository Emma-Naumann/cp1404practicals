"""
Emma Naumann
CP1404 Practical 3
Files
"""

# Question 1
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)


# Question 2
in_file = open("name.txt")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# Question 3
in_file = open("numbers.txt")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)

# Question 4
in_file = open("numbers.txt")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
