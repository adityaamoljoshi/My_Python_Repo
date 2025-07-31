nested = (1,2,3,(4,5,6),(7,8,9,10))
#print(nested[3])
#print(nested[4][3])

      #for loop
#numbers = (2, 5, 67, 83, 54, 68, 98, 56, 78, 99, 100, 101)
#sum=0
#for item in numbers:
    #if item%2==0:
        #sum = sum+item
#print(sum)



     #while loop
numbers = (2, 5, 67, 83, 54, 68, 98, 56, 78, 99, 100, 101)

tlength = len(numbers)-1
counter = 0
sum = 0
while counter < tlength:
    if numbers[counter]%2==0:
        sum= sum+numbers[counter]
    counter += 1
print(sum)

#count method:-


repeatingnum = (1, 1, 2, 2, 2, 3, 3, 3,3, 4, 4, 4, 5, 5, 5)
#print(repeatingnum.count(1))
#print(repeatingnum.count(2))
#print(repeatingnum.count(3))
#print(repeatingnum.count(4))
#print(repeatingnum.count(5))

  #index method:-


indexednum = (1, 4, 7)
print(indexednum.index(1))
print(indexednum.index(4))
print(indexednum.index(7))










