def get_all_keys():
    d = eval(input())
    return list(d.keys()) \
        if d \
        else None


print(get_all_keys())