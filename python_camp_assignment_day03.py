number = 0
five = []

def done_str(a):
    x = a
    print("=========", a + ":Done =========")

# A: Prints out the numbers between 10 and 20 using a loop
while number < 100:
    number = number + 1
    if number > 10 and number < 20:
        print(number)

done_str("A")

# B: Prints out the numbers from 100 to 0 counting backwards by 5’s using a loop
number = 100

while number != 0:
    number = number - 5
    print(number)

done_str("B")

# C: Prints out the numbers 1 through 100 but prints an X for every other number. (using a loop)
number = 0

while number < 105:
    number = number + 4
    if 0 < number <= 100:
        print(number)
    else:
        print("X")
        
done_str("C")

# D: Prints out the numbers 5 - 25 one next to another instead of on separate lines (using a loop)
number = 0
num_str = []
string = ""
while number <= 25:
    if 4 < number < 26:
        num_str.append(number)
    number = number + 1
print(num_str)

for x in num_str:
    string = string + str(x) +' '

print(string)
done_str("D")





