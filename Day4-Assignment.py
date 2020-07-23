#Find all occurence of substring in the given string "What we think we become; we are Python programmer" print the index values.

str = "What we think we become; we are Python programmer"
sub = input("Enter the substring ")
if str.count(sub)==0:
    print("No substring ")
else:
    print("The substrings occured are at:")
    for i in range(len(str)-1):
            if(str[i])+str[i+1]==sub:
                print(i+1)
                i+=1


#Explain using islower() andisupper() with different kinds of strings.

#islower()
#case 1:
str1="Learning"
str1.islower()


#case 2:
str2="learning"
str2.islower()


#case 3:
str3="Learning10"
str3.islower()


#case 4:
str4="12345"
str4.islower()


#case 5:
str5="LEARNING"
str5.islower()


#case 6
str6="learing"
str6.islower()


#isupper()
#case 1:
str1="Learning"
str1.isupper()


#case 2:
str2="learning"
str2.isupper()


#case 3:
str3="Learning10"
str3.isupper()


#case 4:
str4="12345"
str4.isupper()


#case 5:
str5="LEARNING"
str5.isupper()


#case 6
str6="LEARNING10"
str6.isupper()