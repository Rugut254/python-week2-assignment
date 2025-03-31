#step 1: create an empty list
my_list = []

#step 2: append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append(70)
my_list.append(80)
my_list.append(90)

#step 3: insert 15 at second position
my_list.insert(1, 15)

#step 4: extend the list with another list
another_list = [100, 200, 300]

#step 5: remove the last element from the list
my_list.pop()

#step 6:sort the list in ascending order
my_list.sort()

#step 7: find and print the index value of 30
index_30 = my_list.index(30)
print("index of 30:",index_30)