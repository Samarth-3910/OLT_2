def check_apple_key(d):
    if not d or 'apple' not in d:
        return False
    return True


d = input()
print(check_apple_key(d))
