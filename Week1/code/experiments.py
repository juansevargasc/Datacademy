list1 = [1, 2, 3]
list2 = [4, 5, 6]

zipped_lists = zip(list1, list2)

sum = [x + y for (x, y) in zipped_lists]

'''
`zipped_lists` contains pairs of items from both lists
sum = [x + y for (x, y) in zipped_lists]
Create a list with the sum of each pair
'''

print(zipped_lists)
print(sum)