#Assignment Qn.no:1
#To create a new dictionary in which key becomes values and values become keys

dict1 = {21:"ftp",22:"ssh",23:"telnet",80:"http"}
dict2 ={value:key  for key,value in dict1.items()}
print("The output:",dict2)
The output: {'ftp':21,'ssh':22,'telnet':23,'http':80}


#Assignment Qn.no:2
#Make a new list which contains the sum of tuple

list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    list2.append(a+b)
    print("The list contain sum of tuple:",list2)
The list contain sum of tuple: [3, 7, 11, 9]


#Assignment Qn.no:3
#To make the elements in the inner list and tuple to the outer list:

list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print("The required output:",list2)
The required output: [1, 2, 3, 1, 2, 'a', 'hit', 'less']
