# print("Hello World")
# print("Hello EVC")
# print("Hello Class")
# This is my first program in CIT20

a = 10
b = 20

sum = a+b

print(a)
print(b)
print("The Initial sum is " + str(sum))

#overwrite variables
a = 50
b = 100

sum = a+b

print(a)
print(b)
print("The New sum is " + str(sum))

#Naming convention
myName = "Xuan"
my_lastname = "Ho"
print("My name is " + myName + " "+ my_lastname)

first_number = 10
second_number = 20
the_sum = first_number+second_number

print(first_number)
print(second_number)
print("The sum is:", the_sum)

#Arithmetic Operator
theSum = a + b
theDifference = b - a
theMultiplication = a * b
theDivision = b / a
theModulo = 90 % 25
the_integer_quotient = a // b  #return value without remainder

the_sum_in_string = str(the_sum)
#print("The sum is:", theSum)
print("the sum is: " + the_sum_in_string)
print("The difference is:", theDifference)
print("The multiplcation is:", theMultiplication)
print("The division is:", theDivision)
print("The modulo is:", theModulo)
print("The integer quotient:", the_integer_quotient)

#Data Conversion
str()
int()
float()

#Increment (compound assignment)
a = 10
b = 20
c = 30
d = 40

a = a + 1  #a+= 1
b = b - 1  #b-= 1
c = c * 1  #c*= 1
d = d / 1  #d/= 1
print(a)
print(b)
print(c)
print(d)


#Escape Sequences
print("My file is located at C:\\MyDocument")



# separator & end arguments

##input function
your_firstname = input("What is your firstname? : ")
your_lasttname = input("What is your lasttname? : ")
your_address = input("What is your address? : ")
your_city = input("What is your city? : ")
your_zipcode = input("What is your zipcode? : ")
your_state = input("What is your state? : ")

print(your_lasttname + ", " + your_firstname + "\n" +
your_address + "\n" +
your_city + ", " + your_state+ " " + your_zipcode)

##Control Statements
# ==, !=, >, <, >=, <=

##Logical Operators
# AND, OR, NOT

#If Statement
legal_age = input("Enter your age: ")
legal_age = int(legal_age)
legal_age = int(input("Enter your age: "))

if legal_age >= 18:
print("You can vote!")

number_1 = int(input("What is your Number 1: "))
number_2 = int(input("What is your Number 2: "))

if number_1 >= number_2:
diff = number_1 - number_2
print("The different is:",diff)
else:
print("invalid Input")

# Control Statement - If Statement

temp = input("Enter current temperature: ")
temp = int(temp)


if temp>60 and temp<=70:
    print("Temperature is cool")
elif temp>70 and temp<=80:
    print("Temperature is mild")
elif temp>80 and temp<=90:
    print("Temperature is hot")
elif temp > 90:
    print("Temperature is very hot")


# Control Statement - While Loop Statement

print_amount = int(input("Enter Print Amount (1-5): "))

while print_amount > 0 and print_amount< 6:
    print("Hello EVC")
    print_amount= print_amount -1
else:
    print("Number is not 1-5")


user_choice = input("Enter y/n: ")

while user_choice.upper() == "Y":
    print("Hello EVC")



# Control Statement - For Loop + range() function

amount1 = int(input("Print Amount: "))
amount2 = amount1

while amount1 > 0:
    print("Hello 1")
    amount1 = amount1 - 1
print("While Loop Done!")

for i in range(amount2):
    print("Hello 2")
print("For Loop Done!")


# Control Statement - Continue statement (break loop)

choice = input("Enter y/n: ")

while choice.lower() == "y":
    print("No Break Yet")
    break

while choice.lower() != "y":
    print("Not an answer")
    break


counter = int(input("Enter a number: "))

for i in range(0, counter * 2, 2):
    print("My numbers are as follow: "+str(i))


#Defining Function

def add_numbers(a, b):
    print(a + b)

def main():
    print(add_numbers(4, 6))




#List - mutable (modifiable and can have str, int, and float mixed)
list = [0,1.2,"strrr"]

print(list)
print(list[0])
print(list[0] + 2)

#multi-dimensional list
multi_list = []
list_p1 = ["Xuan Ho", "1120 Panoche CT", "4086186670"]
list_p2 = ["Truong Ho", "1120 Panoche CT", "4086695675"]

multi_list.append(list_p1)
print(multi_list)
multi_list.append(list_p2)

for i in multi_list:
    print(i)




# another multi-D example
def main():
    person = []
    people = []

    choice = "y"

    print("=====People Records=====\n")
    while (choice.lower() == "y"):
        name = input("Enter your Name: ")
        address = input("Enter your address: ")
        phone = input("Enter your phone number: ")
        income = input("Enter your income")
        person.append(name)
        person.append(address)
        person.append(phone)

        people.append(person)

        person = []

        choice = input("Continue?(Y/N): ")

    if choice.lower() == "n":
        print("multiD_list: ", people)
        counter = 1
        for i in people:
            print("Person", counter, ":", i)
            counter += 1


main()


# I/O Lesson: OPEN, READ, Write, Close


choice = "y"

while choice.lower() == "y":
    name = input("Enter you name: ")

    #------
    #first method
    outfile = open("test.txt", "a") #open file for writing
    outfile.write(name)
    outfile.close()

    choice = input("Continue? Y/N: ")
    #------

    #second method
    with open("test2.txt", "w") as writefile:
        writefile.write(name)
    with open("test2.txt", "r") as readfile:
        #print("'test2.txt' Line Read:",readfile.readline())
        for line in readfile:
            print(line)


    choice = input("Continue? Y/N: ")


import csv


my_list = [["John", 24], ["Amy", 1], ["Jame", 41]]

with open("test.csv", "w", newline="") as my_file:
    file_object = csv.writer(my_file)
    file_object.writerows(my_list)



people = []
person = []
choice = "y"

while choice.lower() == "y":
    name = input("Enter first name: ")
    age = input("Enter age: ")
    print()

    person.append(name)
    person.append(age)
    people.append(person
                  )
    person = []
    #write people list to a csv file
    with open("name_age.csv", "w", newline="") as my_csv:
        file_object = csv.writer(my_csv)
        file_object.writerows(people)
    #open csv file and read from it
    with open("name_age.csv", newline="") as read_csv:
        file_object = csv.reader(read_csv)
        for l in file_object:
            print(l[0], ",", l[1])

    choice = input("\nContinue? Y/N: ")



def main():

    choice = "y"

    while choice.lower() == "y":
        try:
            a = int(input("Enter on integer: "))
            print("your integer is", a)
            break
        except ValueError:
            print("An integer is required")
            choice = input("\nContinue? Y/N: ")



    print("\nMy program is done!")


main()






