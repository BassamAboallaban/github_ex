# Simple function that we can use to multiply a number by two
def multiply_a_number_by_two(n):
    new_var = n * 2
    return(new_var)


# Function that we can use to calculate compound interest
def compound_interest(base, int_rate, years=5):
    multiplier = 1+int_rate
    amount_ci = base * multiplier ** years
    return(final)
