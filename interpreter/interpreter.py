# Getting the input from the user
interp = input("What do you want to know? ")

# Taking the input from the user and make the variables
x, y, z = interp.split(" ")

# Converting the variables into floats
x_float = float(x)
z_float = float(z)

# Calculating the result of the operation

if y == "+":
    res = x_float + z_float
elif y == "-":
    res = x_float - z_float
elif y == "*":
    res = x_float * z_float
elif y == "/" and z != 0:
    res = x_float / z_float
else:
    print("ZeroDivisionError")

print(round(res,1))