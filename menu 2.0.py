num_one = int(input("Please enter first number: "))

while num_one <= 0:
    num_one = int(input("Please enter valid first number: "))

num_two = int(input("Please enter second number: "))

while num_two <= 0 or num_two < num_one:
    num_two = int(input("Please enter valid second number: "))

options = str(input("Please choose 'E' for even numbers, 'O' for odd numbers, 'S' for squares between the 1st and 2nd number: "))

while options != 'E' and options != 'e' and options != 'O' and options != 'o' and options != 'S' and options != 's':
    options = str(input("Please enter valid option: "))


if options == 'E' or options == 'e':
    for i in range (num_one, num_two):
        if i % 2 == 0:
            print(i, end=" ")
elif options == 'O' or options == 'o':
    for i in range (num_one, num_two):
        if i % 2 != 0:
            print(i, end=" ")

else:
    for i in range (num_one, num_two):
        if i % i**(1/2.0) == 0:
            print(i, end=" ")



