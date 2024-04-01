# phonebill.py
#
# author: C. Maughan
# date: 28/3/24

# This program takes the users amount of airtime mins and texts over
# the month to calculate their phone bill. There is a sales tax of 5%
# over the total. There is an additonal flat charge of $0.44.
airtime = int(input("How many minutes of airtime have you used this month?: "))
texts = int(input("How many texts have you sent this month?: "))
sales_tax = float(5)
base_rate = 1500
text_rate = float(15)
airtime_rate = float(25)
cost_additonal_airtime = float(0)
cost_additonal_text = float(0)
additional_flat_charge = float(44)
subtotal = float(0)



if airtime > 50:
    cost_additonal_airtime = round(((airtime - 50) * airtime_rate) / 100, 2)
    print(f"Your additional airtime cost is: ${cost_additonal_airtime}")

if texts > 50:
    cost_additonal_text = round(((texts - 50) * text_rate) / 100, 2)
    print(f"Your additional text cost is: ${cost_additonal_text}")

print(f"Your base rate is: ${round(base_rate/100, 2)}")
print(f"Your sale tax charge is: {int(sales_tax)}%")
print(f"Your flat charge is: ${additional_flat_charge/100}")
print(f"Your total fee is: {round(((base_rate/100 + additional_flat_charge/100 + cost_additonal_text + cost_additonal_airtime) * 1.05), 2)}")

# My assertions are:

# Texts = 45 and airtime = 45 - base rate = $15.00 - additional airtime null
# additional text cost null - sale tax - 5% - flat charge - $0.44 -
# total - $16.21

# Texts = 55 and airtime = 55 - base rate = $15.00 - additional airtime =
# $1.25 - additional text cost = $0.75 - sale tax = 5% - flat charge =
# $0.44 - total fee = $18.31
