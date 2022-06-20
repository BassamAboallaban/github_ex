# Simple function that we can use to multiply two input numbers 
def multiply_the_2_numbers(a,b):
    new_var = a * b
    return(new_var)


# Function that we can use to calculate compound interest
def compound_interest(base, int_rate, years=10):
    multiplier = 1+int_rate
    final = base * multiplier ** years
    return(final)

