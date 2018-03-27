price_per_kWh_in_cents = float(input("Please enter price per kWh in cents: "))
daily_use_in_kWh = float(input("Please enter the total number of hours the electricity is used in a day: "))

while daily_use_in_kWh > 24:
    daily_use_in_kWh = float(input("Please enter the valid number of hours the electricity is used in a day: "))

num_of_days_for_bill = int(input("Please input the total number of days for billing: "))

num_of_days_for_bill = price_per_kWh_in_cents * daily_use_in_kWh

total_bill = num_of_days_for_bill * num_of_days_for_bill*0.01

print("Estimated bill: $" '{:.2f}'.format(total_bill))