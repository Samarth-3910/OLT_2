def reverse_tuple(t):
    if not t:
        return ()
    return tuple(reversed(t))


t = tuple(map(int, input().split()))
print(reverse_tuple(t))
