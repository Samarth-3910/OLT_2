def get_all_values():
    d = eval(input())
    return list(d.values()) if d else None


print(get_all_values())

# optimized
# def get_all_values():
#     try:
#         d = eval(input())
#         if isinstance(d, dict):
#             return list(d.values())
#         else:
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None
#
# print(get_all_values())