# Simple function that we can use to multiply two input numbers 
def multiply_the_2_numbers(a,b):
    new_var = a * b
    return(new_var)


# Function that we can use to calculate compound interest
def compound_interest(base, int_rate, years=5):
    multiplier = 1+int_rate
    amount_ci = base * multiplier ** years
    return(amount_ci)