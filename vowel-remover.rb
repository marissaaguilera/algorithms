
# Create a function called shortcut to remove all the lowercase vowels in a given string.



def shortcut s

    s.delete('aeiou')

end

puts(shortcut('hello')) #,'hll')
puts(shortcut('HELLO')) #,'HELLO')