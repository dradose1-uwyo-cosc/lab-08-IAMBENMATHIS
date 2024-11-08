# Benjamin
# UWYO COSC 1010
# 11/8/2024
# Lab 08
# Lab Section: 10
# Sources, people worked with, help given to: Jackson, Austin Barner, Paige the TA
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_to_number(num):
    """does the stuff"""
    num = num.replace(" ", "")
    is_neg = False
    if num[0] == "-":
        is_neg = True
        num = num.replace("-", "")
    if "." in num:
        nums = num.split(".")
        if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
            if is_neg:
                return -1 * float(num)
            else: 
                return float(num)
    elif num.isdigit():
        if is_neg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False

def slope_intercept(m, b, up_x, low_x):
    """Does the thing"""
    calc_list = []
    if type(up_x) and type(low_x) == int and up_x > low_x:
        for calc in range(low_x, up_x):
            calc_list.append(m*calc + b)
        return calc_list
    else:
        print("Your upper bound must be greater than your lower bound and both must be ints.")

def sqr(num):
    "squares a given number"
    if num < 0:
        return None
    else:
        return num ** (1/2)        

def quad_form(a, b, c):
    """Completes the quadratic formula and returns two values"""
    outcome_list = []
    zorp = 0
    #(-b - sqr((b**2) - (4*a*c))) / (2*a)
    zorp = sqr((b**2) - (4*a*c))
    if zorp == None:
        print("imaginary number!")
        return None
    #(-b + sqr((b**2) - (4*a*c))) / (2*a)
    outcome_list.append((-b - zorp) / (2*a))
    outcome_list.append((-b + zorp) / (2*a))
    return outcome_list


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list




active = True
while active:
    print("enter exit to end program")
    m = input("please input: slope: ")
    if m.lower() == "exit":
        break
    m = convert_to_number(m)
    if type(m) == bool:
        print("All entries must be numbers")
        continue

    b = input("please input: intercept: ")
    if b.lower() == "exit":
        break
    b = convert_to_number(b)
    if type(b) == bool:
        print("All entries must be numbers")
        continue
    up_x = input("please input: upper bound of x: ")
    if up_x.lower() == "exit":
        break
    up_x = convert_to_number(up_x)
    if type(up_x) == bool:
        print("All entries must be numbers")
        continue
    low_x = input("please input: lower bound of x: ")
    if low_x.lower() == "exit":
        break
    low_x = convert_to_number(low_x)
    if type(low_x) == bool:
        print("All entries must be numbers")
        continue
    
    
    
    

    print(type(m), type(b), type(up_x), type(low_x))
        
    
    listlist = slope_intercept(m, b, up_x, low_x)
    print(listlist)


print("*" * 75)



# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

active = True
while active:
    print("enter exit to end program")
    
    a = input("please input: a: ")
    if a.lower() == "exit":
        break
    a = convert_to_number(a)
    if type(a) == bool:
        print("All entries must be numbers")
        continue
    
    b = input("please input: b: ")
    if b.lower() == "exit":
        break
    b = convert_to_number(b)
    if type(b) == bool:
        print("All entries must be numbers")
        continue

    c = input("please input: c: ")
    if c.lower() == "exit":
        break
    c = convert_to_number(c)
    if type(c) == bool:
        print("All entries must be numbers")
        continue
  
        
    result_list = quad_form(a, b, c)
    print(result_list)

 