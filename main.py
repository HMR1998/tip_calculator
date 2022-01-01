print("Welcome to the tip calculator.")

total = float(input("What was the total bill?"))
print("£",total)

split = float(input("How many people to split the bill?"))
print(split)

tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15?"))
print("£",tip_percent)

bill_split = total / split


tip_decimal = tip_percent / 100

tip_amount = bill_split * tip_decimal

tip_and_bill = tip_amount + bill_split

print(f"You should pay: £{round(tip_and_bill, 1)}")