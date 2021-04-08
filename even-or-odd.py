

# Given a string of digits confirm whether the sum of all the individual 
# even digits are greater than the sum of all the indiviudal odd digits. 
# Always a string of numbers will be given.

# If the sum of even numbers is greater than the odd numbers return: 
# "Even is greater than Odd"

# If the sum of odd numbers is greater than the sum of even numbers return: 
# "Odd is greater than Even"

# If the total of both even and odd numbers are identical return: 
# "Even and Odd are the same"


def even_or_odd(s):
    """Given a string of numbers find the sum and compare."""

    ecount = 0 
    ocount = 0
    final = ''

    for digit in s: 
        d = int(digit)

        if d % 2 == 0:
            ecount += d
        else:
            ocount += d
    
    if ecount > ocount:
        final = "Even is greater than Odd"
    elif ocount > ecount:
        final = "Odd is greater than Even"
    elif ecount == ocount: 
        final = "Even and Odd are the same"
    return final


print(even_or_odd('12')) #, 'Even is greater than Odd'
print(even_or_odd('123')) #, 'Odd is greater than Even'
print(even_or_odd('112')) #, 'Even and Odd are the same'