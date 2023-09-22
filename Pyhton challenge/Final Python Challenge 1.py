#Assign an integer to a variable:

num1 = int(30)

#Assign an string to a variable:

name= "Josiah"

#Assign an float to a variable:

float= 2.5

#Print statement to print the variables created

print(name + " is " + str(num1) + " years old. Their age divided by the float variable is "
      + str(num1 / float) + ".")


#Using math operators:

number1 = 14
number2 = 28
number3 = 120
number4 = 2

print("Number3 divided by Number4 equals " + str(number3 / number4))
print("Number2 added to Number1 is equal to " + str(number2 + number1))
print("Number4 multiplied by Number1 equals " + str(number4 * number1))
print("The remainder of Number3 divided by Number2 equals " + str(number3 % number2))

#Using logical operators:

price = 10
print(price > 2 and price < 25)
print(price > 30 or price == 10)
print(not price > 100)

#Using conditional statements

temperature = 5
if temperature > 30:
    print( "It's very hot outside")
    print( "Make sure to drink plenty of water")
elif temperature > 20:
    print( "It's a nice day outside")
elif temperature > 13:
    print( "It's a bit chilly outside")
else:
    print( "It's cold outside")

#Using a while loop

age = int(input(" Please enter your age: "))
while age < 0:
    print("Age can't be negative")
    age = int(input(" Please enter your age: "))
print("You are " + str(age) + " years old")

#Using a for loop to iterate through a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in numbers:
    print(item)

#Using a for loop to iterate through a tuple

sports_tuple = ('basketball','soccer','volletball','baseball','swimming')

for sports in sports_tuple:
    print(sports)

#Defining a function that returns a string value + Calling the fucntion and printing the result

def my_function():
   print("josey")

my_function()
print('Hello World')


    
    
    
    












