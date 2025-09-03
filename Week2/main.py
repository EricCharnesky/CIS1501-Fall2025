import math
import random

name = input("Enter your name")

print("Hi there", name)
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))
print("Roll a 6 sided die:", random.randint(1, 6))

# ** is exponential
print("square root of 90:", 90**.5)

print("Hello world!")

print("Happy wednesday!")

print("Week 2 is almost over already?!?")

print(5 * 2)

print( 7 + 2)

print( 11 / 3)

print( 27 - 15)

print( 9 / 3 * (9 / 3) )

wage = float(input("enter your hourly wage"))

print("In 40 hours you would make", wage * 40)

weekly_hours = float(input("enter your average hours worked each week"))


weekly_salary = weekly_hours * wage

print("In a week, you would make $", weekly_salary)

TAX_RATE = .15

weekly_salary_after_tax = weekly_salary * ( 1 - TAX_RATE )

print("After taxes, your take home pay is:", weekly_salary_after_tax)

PAID_WEEKS_PER_YEAR = 50

annual_salary_after_tax = weekly_salary_after_tax * PAID_WEEKS_PER_YEAR

monthly_rent = int(input("Enter your monthly rent"))
monthly_utilities = int(input("Enter your monthly utility bill"))
monthly_car_payment = int(input("Enter your monthly car payment"))
monthly_insurance = int(input("Enter your monthly insurance bill"))
monthly_food = int(input("Enter your monthly food bill"))
monthly_gas = int(input("Enter your monthly gas bill"))

annual_bills = (monthly_rent + monthly_utilities + monthly_car_payment +
                monthly_insurance + monthly_food + monthly_gas) * 12

left_over = annual_salary_after_tax - annual_bills

print("After your bills, you'll have: $", left_over)

# integer remainder - modulus
print( "remainder of 5 / 2 is:", 5 % 2 )

print("square root of 90:", math.sqrt(90))