def divisible_by_11(number):
    """Uses above criterion to check if number is divisible by 11"""
    string_number = str(number)
    alternating_sum = sum([(-1) ** i * int(d) for i, d
                           in enumerate(string_number)])
    return alternating_sum == 0


#----------------

# corrected version
def divisible_by_11(number):
    """Uses above criterion to check if number is divisible by 11"""
    string_number = str(number)
    # Using abs as the order of the alternating sum doesn't matter.
    alternating_sum = abs(sum([(-1) ** i * int(d) for i, d
                               in enumerate(string_number)]))
    # Recursively calling the function
    return (alternating_sum in [0, 11]) or divisible_by_11(alternating_sum)