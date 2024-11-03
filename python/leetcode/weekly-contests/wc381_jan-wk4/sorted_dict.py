my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)

