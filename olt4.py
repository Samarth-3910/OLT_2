# Sample Input:{'apple':'red', 'banana':'yellow', 'orange':'orange'}
# Sample Output:{'apple':'red', 'banana':'yellow', 'orange':'orange', 'grape':'purple'}

def add_grape_pair(d):
    d['grape'] = 'purple'
    return d


input_dict = eval(input())

output_dict = add_grape_pair(input_dict)

print(output_dict)
