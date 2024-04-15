def find_keys_with_max_value(d):
    if not d:
        return None

    max_value = max(d.values())
    max_keys = [key for key, value in d.items() if value == max_value]

    return max_keys


d = eval(input())
print(find_keys_with_max_value(d))
