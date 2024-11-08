#----1-----given values and keys convert into list of dictionaries and sort them
# inp_lt=['morning',1,'evening',3,'afternoon',2]
# key_lt=['phase','id']
# lt=[]
# for i in range(0,len(inp_lt),2):
#     lt.append({key_lt[0]:inp_lt[i],key_lt[1]:inp_lt[i+1]})
# lt.sort(key=lambda x:x['id'])
# print(lt)

#------2-----find common in two lists and store in new list
# lt1=map(int,list(input("enter list items for list1: ").split()))
# lt2=map(int,list(input("enter list items for list2: ").split()))
# new_lt=list(set(lt1)&set(lt2))
# new_lt.sort()
# print(new_lt)


#----3-----write prg to check list is sorted in asc or not
# lt=list(map(int,input("enter list: ").split()))
# lt1=lt.copy()
# lt1.sort()
# if lt1==lt:
#     print("The list is sorted")
# else:
#     print("list is not sorted")

#-----4--count occurances of each element
# lt=list(map(int,input("enter list : ").split()))
# lt.sort()
# lt1=set(lt)
# for i in lt1:
#     print(f"count of {i} is {lt.count(i)}")

#-----5---concatenate lists
# lt1=list(map(int,input("enter list items1: ").split()))
# lt2=list(map(int,input("enter list items2: ").split()))
# print(lt1+lt2)

#----6----find max and min in list
# lt1=list(map(int,input("enter list items: ").split()))
# print(max(lt1))
# print(min(lt1))

#-----8---count char of each string using dictinary
# s1="".join(input("enter a string: "))
# dic={}
# for i in s1:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)


#---9---set union intersection and difference
# set1={1,2,3,2,4}
# set2={4,5,6,4}
# print(set1 & set2)
# print(set1-set2)
# print(set1|set2)

#---10---function that pops key value from dict
# def remove(dic,key):
#     dic.pop(key)
#     return dic
# dic={'hema':1234,"hem":123}
# print(remove(dic,'hem'))


#---11---prg takes two lists and give dic of ele count
# lt1=list(map(int,input("enter list items1: ").split()))
# lt2=list(map(int,input("enter list items2: ").split()))
# lt3=lt1+lt2
# dic={}
# for i in lt3:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1

# print(dic)


###Hands-on-4#####
# ---1----split the string and print in new lines
# str1=input("enter a sentence: ") 
# for i in str1.split(" "):
#     print(i)

#----2-----program to reverse order of words
# lt=list(input("enter a sentence: ").split())
# lt=lt[::-1]
# print(' '.join(lt))

#----3----prg to reverse internal content of string
# str1=list(input("enter a sentence: ").split())
# s=''
# for i in str1:
#     s+=i[::-1]+" "
# print(s)

#-----4----program for a2b3c2 as aabbbcc
# ip=input("enter string: ")
# lt,lt1=[],[]
# for i in ip:
#     if i.isdigit():
#         lt.append(i)
#     else:
#         lt1.append(i)
# s=''
# for i in range(len(ip)//2):
#     s+=lt1[i]*int(lt[i])
# print(s)

