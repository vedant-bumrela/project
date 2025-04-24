items = [
    ("item1", 10),
    ("item2", 9),
    ("item3", 11),
    ("item4", 7),
]

# def sort_items(items):
#     return items[1]
    

# items.sort(key=sort_items,reverse=True)
# print(items)

# sortd_list = sorted(items, key=lambda x: x[1])
# print(sortd_list)

x = map(lambda x: x[1], items)
print(list(x))
print([item[1] for item in items])

y = filter(lambda x: x[1] > 9,items)
print(list(y))
print([item for item in items if item[1] > 9])

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]

print(list(zip(list1, list2, list3)))