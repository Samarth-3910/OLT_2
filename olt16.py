def str_rev(s):
    if not s:
        return None
    return ''.join(reversed(s))

s = input()
print(str_rev(s))