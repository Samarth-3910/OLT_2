#to remove duplicate values from dictionary it includes duplicate values, empty dictionary and dictionary with duplicate values associated with different keys
def remove_duplicate_values(d):
    if not d:
        return None

    unique_values = set()
    unique_d = {}
    for key, value in d.items():
        if value not in unique_values:
            unique_values.add(value)
            unique_d[key] = value

    return unique_d

d = eval(input())
print(remove_duplicate_values(d))
