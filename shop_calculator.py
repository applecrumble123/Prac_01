num_of_items = int(input("Please enter the number of items you want: "))

while num_of_items < 0:
    num_of_items = int(input("Please enter a valid number: "))

sum = 0.00

for i in range (num_of_items):
    item_price = float(input("Please enter price of item: "))
    while item_price <= 0:
        item_price = float(input("Please enter valid price of item: "))
    sum = sum + item_price

if sum > 100:
    print("The total price of the", num_of_items, "items is $" '{:.2f}'.format(sum*0.9))
else:
    print("The total price of the", num_of_items, "items is $" '{:.2f}'.format(sum))

