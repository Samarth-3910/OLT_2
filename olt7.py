def sum_even_numbers(t):
    if not t:
        return None
    return sum(x for x in t if x % 2 == 0)


t = tuple(map(int, input().split()))
print(sum_even_numbers(t))
