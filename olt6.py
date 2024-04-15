def are_elements_unique(tuple_or_str):
    return len(set(tuple_or_str)) == len(tuple_or_str)

t = tuple(input().split())
print(are_elements_unique(t))
