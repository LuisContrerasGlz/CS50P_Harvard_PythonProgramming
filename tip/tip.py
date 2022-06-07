def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    without_dollar_s = d.replace("$", "")
    return float(without_dollar_s)


def percent_to_float(p):
    without_per_s = p.replace("%", "")
    return float(without_per_s) / 100


main()