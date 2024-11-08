#lists-task-1
# lt=[]
# print("Fruits Menu")
# print("------------")
# print("1.Display list\n2.Add a fruit\n3.Search a fruit\n4.Delete a fruit\n5.Edit list\n6.Exit")
# choice=0
# while choice!=6:
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         print(lt)
#     elif choice==2:
#         add=input("enter fruit name: ")
#         lt.append(add)
#     elif choice==3:
#         search=input("enter fruit that is to be searched: ")
#         ind=lt.index(search)
#         print("the index of fruit is",ind)
#     elif choice==4:
#         delte=input("enter fruit name to delete: ")
#         lt.remove(delte)
#     elif choice==5:
#         ind,name=input("enter index and name of fruit to insert in list: ").split(" ")
#         lt.insert(int(ind),name)

#---1--create,access,length,append,inser list
# lt=[]
# for i in range(1,11):
#     lt.append(i)
# print(lt)
# print(lt[0])
# print(lt[2])
# print(lt[-1])
# print(len(lt))
# lt.append(11)
# lt.insert(1,'second')
# print(lt)

#----2----remove,slice,concate,comprehend,max,min
# lt.remove(9)
# print(lt[0:3])
# print(lt[-3:])
# l1=[9,0,0]
# l2=lt+l1
# print(l2)
# print(min(lt))
# print(max(lt))
# print(sum(lt))


#-------List tasks without using methods-------

#--1--list takes 10 input integers and display max,second max,asc,desc,search for element
# lt=[]
# for i in range(10):
#     lt.append(int(input(f"enter number {i+1}: ")))
# #implemnting bubble sort to sort list of 10 ele
# for i in range(10):
#     for j in range(10-i-1):
#         if lt[j]>lt[j+1]:
#             lt[j],lt[j+1]=lt[j+1],lt[j]
# print(lt[-1])#max ele
# print(lt[-2])#second max
# print(lt)#ascending order
# print(lt[-1::])#descending order
#searching an element
#implementing binary search
# ele=int(input("enter number to get index in list: "))
# def binsearch(ele,lt,st=0,la=9):
#     if st>la:
#         return -1
#     mid=(st+la)//2
#     if lt[mid]==ele:
#         return mid+1
#     elif lt[mid]>ele:
#         return binsearch(ele,lt,0,mid-1)
#     else:
#         return binsearch(ele,lt,mid+1,9)
# res=binsearch(ele,lt)
# print(res)


#----dictionary task------
#----menu driven program-------
# print("Employee Menu")
# print("--------------")
# print("1.Display dictionary\n2.search emp by id\n3.add an emp\n4.edit an emp\n5.delete an emp by id\n6.exit")
# choice=0
# emplt=[]
# while choice!=6:
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         for i in emplt:
#             print(i)
#     elif choice==2:
#         empid=int(input("enter id to get emp info"))
#         for i in emplt:
#             if i['id']==empid:
#                 print(i)
#     elif choice==3:
#         dic={}
#         dic['id']=int(input("enter emp id: "))
#         dic['ename']=input("enter ename: ")
#         dic['job']=input("enter emp job: ")
#         dic['salary']=int(input("enter emp salary: "))
#         emplt.append(dic)
#     elif choice==4:
#         editid=int(input("enter id of emp to edit: "))
#         for i in emplt:
#             if i['id']==editid:
#                 edittype,editvalue=input("enter key  and value to edit: ").split(" ")
#                 if editvalue.isnumeric():
#                     i[edittype]=int(editvalue)
#                 else:
#                     i[edittype]=editvalue
            
#     elif choice==5:
#         delid=int(input("enter id of emp to delete: "))
#         for i in emplt:
#             if i['id']==delid:
#                 emplt.remove(i)

