TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Please enter 11 for 'Tariff 11' or 31 for 'Tariff 31): "))

while tariff != 11 and tariff != 31:
    tariff = int(input("Please input valid tariff number:"))

daily_use_in_kWh = float(input("Please enter the total number of hours the electricity is used in a day: "))

while daily_use_in_kWh > 24:
    daily_use_in_kWh = float(input("Please enter the valid number of hours the electricity is used in a day: "))

num_of_days_for_bill = int(input("Please input the total number of days for billing: "))

if tariff == 11:
    total_cost = TARIFF_11 * daily_use_in_kWh * num_of_days_for_bill
else:
    total_cost = TARIFF_31 * daily_use_in_kWh * num_of_days_for_bill


print("Estimated bill: $" '{:.2f}'.format(total_cost))