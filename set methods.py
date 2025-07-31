 #Add function

words = {"hello", "bye"}
words.add("thanks")
print(words)
 #remove function

words_2 = {"q", "w", "e"}
words_2.remove("w")
print(words_2)
#NOTE: Discard function will do the same thing as remove but will  ot give an error message if removed a non exist item of a set


 #clear function: it will make a set to empty set

words_3 = {"q", "w", "e", "t"}
words_3.clear()
print(words_3)

 #copy function

set_1= {"a", "b", "c"}
set_2 = set_1.copy()
print(set_2)
print(set_2 is set_1)

 #union function

set_3 = {1, 2, 3}
set_4 = {4, 5, 6}
set_5 = set_3.union(set_4)
print(set_5)

set_6 = set_3|set_4      #{|}  this is called pipe character
print(set_6)


 #intersection function

set_7 = {1, 2, 3, 4, 5}
set_8 = {2, 3, 4, 5, 6, 7, 8}

set_9 = set_7.intersection(set_8)
print(set_9)

set_10 = set_7 & set_8
print(set_10)


 #substraction and differance functions

set_7 = {1, 2, 3, 4, 5}
set_8 = {2, 3, 4, 5, 6, 7, 8}

set_11 = set_8 - set_7
print(set_11)

set_12 = set_8.difference(set_7)
print(set_12)

 #Comprehensions: Advance set formations
comp_1 = {even+2 for even in set(range(0, 14, 2))}
print(comp_1)

set_b= {"A", "B", "C"}
comp_2 ={char.lower() for char in set_b}
print(comp_2)

