set_1 = {1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5}
set_2 =set({"a", "b", "c", "d"})
print(set_1)
print(set_2)
for num in set_1:
    print(num)

#for empty set we need to give set function or it will make it a dictionery

set_3 = set()
print(set_3)

#callin rage function in set:-

set_4 = set(range(0, 13, 2))
set_5 = set(range(1, 14, 2))
print(set_4)
print(set_5)

#set can hold differant data types

set_6 = {"a", 3.18, 70, False}
print(set_6)
print(3.18 in set_6)