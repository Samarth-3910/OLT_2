def str_rev(s):
    if not s:
        return None
    return s.lower()[::-1]\
        if any(c.isupper() for c in s) \
        else s[::-1]

print(str_rev(input()))
