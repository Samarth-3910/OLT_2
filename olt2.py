def find_max_in_tuple(t):
    if not t:
        return None  # or any other value you want to return for an empty tuple
    return max(t)

t = tuple(map(eval, input().split()))
print(find_max_in_tuple(t))