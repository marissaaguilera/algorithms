

# It's pretty straightforward. Your goal is to create a function that removes 
#the first and last characters of a string. You're given one parameter, 
#the original string. You don't have to worry with strings with less than 
#two characters.

def remove_char s

    s[1...-1]

end

puts(remove_char('eloquent')) #, 'loquen')
puts(remove_char('country')) #, 'ountr')
puts(remove_char('person')) #, 'erso')
puts(remove_char('place')) #, 'lac')
puts(remove_char('ok')) #, '')