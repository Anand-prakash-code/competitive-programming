tup1=(20,)
print(tup1) #(20,)
print(type(tup1)) #<class 'tuple'>
 
numbers=(10,2,3)
print(numbers[0]) #10
print(numbers[2]) #3
print (numbers[-1]) #3

tup =(10,[2,3,4],8,9)
tup[2].append(400) #invalid bcz tuples are immutable
tup[1].append(400)
tup[1].append(400)
print(tup)          #(10, [2, 3, 4, 400, 400], 8, 9)


