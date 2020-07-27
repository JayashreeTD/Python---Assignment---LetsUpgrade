#Day6 Assignment:

#List1=[1,2,3,4,5,7,8]
#List=["a","b","c","d","e"]
#convert to a dicitionary in one line code using list comprehension (without using zip method)

list1=[1,2,3,4,5,6,7,8]
list2=["a","b","c","d","e"]
dic1={}
print({list1[each] : list2[each] for each in range(min(len(list1),len(list2)))})
