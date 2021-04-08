

# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> 
# String, which must take in input array, containing the names 
# of people who like an item. It must return the display text as 
# shown in the examples:



def likes_it(names):
    """Implement the text that appears when someone likes something (EX.Facebook)."""

    text = ""
    length = len(names)

    if length == 0:
        text = "no one likes this"

    elif length == 1:
        text = f"{names[0]} likes this"

    elif length == 2:
        text = f"{names[0]} and {names[1]} like this"   

    elif length == 3:
        text = f"{names[0]}, {names[1]} and {names[2]} like this"

    else:   
        text = f"{names[0]}, {names[1]} and {length - 2} others like this"

    return text


print(likes_it([])) #"no one likes this"
print(likes_it(["Peter"])) #"Peter likes this"
print(likes_it(["Jacob", "Alex"])) #"Jacob and Alex like this"
print(likes_it(["Max", "John", "Mark"])) #"Max, John and Mark like this"
print(likes_it(["Alex", "Jacob", "Mark", "Max"])) #"Alex, Jacob and 2 others like this"