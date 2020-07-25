#Question 1 :

#[0,1,2,10,4,1,0,56,2,0,1,3,0,1,3,0,56,0,4] 
#sort by increasing order but all zeros should be at the right hand side.

list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list1.sort()
list1.extend((0,0,0,0,0))
del list1[0:5]
print(list1)


#Question 2: 

#list1=[10,20,40,60,70,80] sorted list.
#list2=[5,15,25,35,45,60]  sorted list.
#Merging the sorted lists using for loop to get sorted output.

list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
res=list1+list2
for each in range(5,81):
    if each in res:
        print(each,end=",")