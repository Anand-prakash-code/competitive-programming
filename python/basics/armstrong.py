# check armstrong no

n= input ("enter number:") #returns a string not a int 

d=int (n)
x=len(n)
sum =0

while d>0:
  t = d%10
  sum = sum + t**x
  d = d//10

if sum ==int (n):
  print(n ,"is a armstrong number ")
else:
  print(n ,"is not a armstrong number")

