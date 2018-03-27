name = str(input("Please enter your name: "))

options = str(input("Please choose 'H', 'G', or 'Q': "))

while options != 'H' and options != 'h' and options != 'G' and options != 'g' and options != 'q' and options != 'Q':
    options = str(input("Please enter valid option: "))

if options == 'H' or options == 'h':
    print("Hello", name)
elif options == 'G' or options == 'g':
    print("Goodbye", name)
else:
    print("Finished")