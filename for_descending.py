'''
Created on Apr 17, 2019

@author: user
'''
# Python Program to Sort List in descending Order

numlist=[]

number=int(input("please enter total number list:"))
for i in range(1,number+1):
    value=int(input("please enter the value of %d elelment:"%i))
    numlist.append(value)

for i in range(1):
    for j in range(i+1,number):
        if(numlist[i])>(numlist[j]):
            temp=numlist[i]
            numlist[i]=numlist[j]
            numlist[j]=temp
            
print("element after sorting list in descending order is:",numlist)            
