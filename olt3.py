# write a program in dictionary  to access the value associated with the key 'banana' in the dictionary.
# Take user input for the dictionary and print the value associated with the key 'banana'.
def get_banana_value():
    d = eval(input())
    if not d or 'banana' not in d:
        return None
    return d.get('banana')

print(get_banana_value())
