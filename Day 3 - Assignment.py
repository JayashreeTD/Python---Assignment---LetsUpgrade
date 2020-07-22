#!/usr/bin/env python
# coding: utf-8




# Assignment 1 : Sum of n numbers with help of while loop.

n=int(input("Enter n:"))
sum=0
c=1
while c<=n:
    print(c)
    sum=sum+c
    c=c+1
print("Sum of 1 to n =",sum)    





# Assignment 2 : Prime number or not.

n=int(input("Enter n: "))
c=0
for i in range(2,n,1):
    if n%i == 0:
        c=c+1
if c==0:
    print("Prime number ")
else:
    print("Not Prime number ")












