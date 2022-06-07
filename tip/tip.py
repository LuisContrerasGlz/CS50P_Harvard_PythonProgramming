# It’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. 

# Main function for calculator it asks for the cost of the meal and % of the tip calling the functions for it and then calculates the total
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Accepts a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float
def dollars_to_float(d):
    without_dollar_s = d.replace("$", "")
    return float(without_dollar_s)

# Accepts a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float
def percent_to_float(p):
    without_per_s = p.replace("%", "")
    return float(without_per_s) / 100


main()