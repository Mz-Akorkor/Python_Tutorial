# 1. Create variables
x = 15
y = 4

sum = x + y
difference = x - y
product = x * y
quotient = x / y 

# 2. Print results
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# 3. Calculate the square of a number and print
number = 10
sqaure = number ** 2
print("Square of", number, "is:", sqaure)

# 4. Find the remainder when 27 is divided by 4
remainder = 27 % 4
print("Remainder when 27 is divided by 4 is:", remainder,)

# 5. Convert the float 3.75 into an integer
float_num = 3.75
int_num = int(float_num)
print("Integer version of 3.75 is:", int_num)

# 6. Convert the integer 7 into a float.
int_num = 7
float_num = float(int_num)
print("Float version of", int_num, "is:", float_num)

# 7. Round the number 12.6789 to 2 decimal places
rounded_num = round(12.6789, 2)
print("Rounded number is:", rounded_num)

# 8. Find the absolute value of -23.4.
abs_value = abs(-23.4)
print("Absolute value is:", abs_value)

# 9. Use divmod() to return the quotient and remainder of 20 divided by 3.
quotient, remainder = divmod(20, 3)
print("Quotient:", quotient)
print("Remainder:", remainder)

# 10. Multiply a float by an integer: 3.5 × 4.
result = 3.5 * 4 
print("3.5 multipled by 4 is:", result)

# 11. Use exponentiation to calculate 5 raised to the power of 3.
power = 5 ** 3 
print("5 raised to the power of 3 is:", power)

# 12. Calculate the area of a circle with radius 5. Use πr²
import math
radius = 5
area = math.pi * (radius ** 2)
print("Area of the circle is:", round(area, 2))

# 13. Convert a temperature of 100°C to Fahrenheit using the formula:
celsius = 100
fahrenteit = (celsius * 9/5) + 32
print("Temperature in Fahrenteit is:", fahrenteit)

# 14. Calculate the monthly interest on a loan of GHS 2000 at an annual interest rate of 12%.
loan = 2000
annual_interest_rate = 0.12
monthly_interest_rate = annual_interest_rate / 12
monthly_interest = loan * monthly_interest_rate
print("Monthly interest on the loan is: GHS", round(monthly_interest, 2))

# 14. You have $200 and want to split it evenly among 3 friends.
total_amount = 200
friends = 3

each_gets = total_amount // friends
remainder = total_amount % friends

print("Each friend gets: GHS", each_gets)
print("Remainder: GHS", remainder)

# 15. A car travels 120 km in 2.5 hours
distance_km = 120
time_hours = 2.5

average_speed = distance_km / time_hours
print("Average speed is:", average_speed, "km/h")

