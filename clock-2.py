

# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

# Your task is to make 'Past' function which returns time converted to milliseconds.

#Codewars Problem: Beginner series clock #2 

def past(h, m, s):
    """Given an hour, minute, and second return the time in milliseconds."""

    # 1000 milliseconds in a second 
    # 60,000 milliseconds in a minute 
    # 3,600,000 milliseconds in a hour 

    second = 1000 
    minute = 60000
    hour = 3600000

    # return (3,600*h + 60*m + s) *1,000

    # return (3600*h + 60*m + s) * 1000

    millisecond = (h * hour) + (m * minute) + (s * second)

    return millisecond

print(past(0,1,1)) #,61000)
print(past(1,1,1)) #,3661000)
print(past(0,0,0)) #,0)
print(past(1,0,1)) #,3601000)
print(past(1,0,0)) #,3600000)