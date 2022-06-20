# Simple function that we can use to multiply a number by two
def multiply_a_number_by_two(n):
    new_var = n * 2
    return(new_var)


# Function that we can use to calculate compound interest
def compound_interest(base, int_rate, years=10):
    multiplier = 1+int_rate
    final = base * multiplier ** years
    return(final)