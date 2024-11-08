#task-1 using while loop
# i=1
# while 1<=i<=5:
#     print(i)
#     i+=1

# i=5
# while 1<=i<=5:
#     print(i)
#     i-=1

#task-2 calculate factorial of given number
# num=int(input("enter a number: "))
# n=num
# fact=1
# if num==1 or num==0:
#     fact=1
# else:
#     while num!=1:
#         fact*=num
#         num-=1
# print(f"factorial of {n} is {fact}")

# task-3 fibonacci series upto given limit

# num=int(input("enter a limit to have the fibonnaci series: "))
# n1=0
# n2=1
# if num==1:
#     print(n1,end=" ")
# elif num==2:
#     print(n1,end=" ")
#     print(n2, end=" ")
# else:
#     print(n1,end=" ")
#     print(n2,end=" ")
#     while num!=2:
#         temp=n1+n2
#         print(temp,end=" ")
#         n1=n2
#         n2=temp
#         num-=1

# dispaly table for the input number

# num=int(input("enter a number: "))
# i=1
# while i<=10:
#     print(f"{num} x {i} = {num*i}")
#     i+=1

#perform arthemitic operations based on the choice

# a=int(input("enter number a: "))
# b=int(input("enter number b: "))
# print("select any of the operation: ")
# print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit")
# choice=0
# while choice!=5:
#     choice=int(input("Enter choice: "))
#     if choice==1:
#         print(f"addition of {a} {b} is {a+b}")
#     elif choice==2:
#         print(f"subtraction of {a} {b} is {a-b}")
#     elif choice==3:
#         print(f"multiplication of {a} {b} is {a*b}")
#     elif choice==4:
#         print(f"division of {a} {b} is {a//b}")


#read a number and display in words

# num=int(input("enter a two digit number: "))
# n=num
# a=n%10
# n=num//10
# b=n%10
# if b==1 or a==0:
#     dic1={11:'eleven',12:'tweleve',13:"thirteen",
#           14:"fourteen",15:"fifteen",16:"sixteen",
#           17:"seventeen",18:"eighteen",19:"nineteen",
#           10:"ten",20:"twenty",30:"thirty",40:"fourty",
#           50:"fifty",60:"sixty",70:"seventy",80:"eighty",
#           90:"ninty"}
#     print(dic1[num]," only")
# else:
#     dicb={2:"twenty",3:"thirty",4:"fourty",
#           5:"fifty",6:"sixty",7:"seventy",8:"eighty",
#           9:"ninty"}
#     dica={1:"one",2:"two",3:"three",4:"four",5:"five",
#           6:"six",7:"seven",8:"eight",9:"nine"}
#     print(dicb[b]," ",dica[a],"only")

#task-6 handling integer
#count the digits and even digits in a number aslo thier sum
# num=int(input("enter a number: "))
# i,ic=0,0
# j,jc=0,0
# while num>0:
#     n=num%10
#     i+=n
#     ic+=1
#     if n%2==0:
#         j+=n
#         jc+=1
#     num//=10
# print(f"sum of digits is {i} and their count is {ic}")
# print(f"sum of even digits is {j} and their count is {jc}")


#task-6 count factors of number
# num=int(input("enter a number: "))
# i,c=2,0
# while i<num:
#     if num%i==0:
#         c+=1
#     i+=1
# if c:
#     print("the no.of factors are ",c)
# else:
#     print("there are no factors")


#task-7 reverse an integer and check it is palindrome or not
# num=int(input("enter a number: "))
# num1=num
# lt=[]
# while num>0:
#     n=num%10
#     lt.append(n)
#     num//=10
# num2=int(''.join(map(str,lt)))
# print("reverse number is",num2)
# if num1==num2:
#     print("it is palindrome number")
# else:
#     print("not a palindrome number")

#task-8 perfect number and armstrong number
# num=int(input("enter a number: "))
# sum=1
# for i in range(2,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print("the number is a perfect number")
# else:
#     print("the number is not perfect number")

#armstrong number
# num=int(input("enter a three digit number: "))
# n,sum=num,0
# for i in range(3):
#     a=n%10
#     sum+=a**3
#     n//=10
# if sum==num:
#     print("it is an armstrong number")
# else:
#     print("not an armstrong number")