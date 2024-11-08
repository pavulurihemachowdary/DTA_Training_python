#----hands-on-1----------#
# from datetime import datetime, date

# def find_age(birth):
#     # Convert the birthdate string to a datetime object using strptime, then extract the date part
#     birth1 = datetime.strptime(birth, "%Y-%m-%d").date()
    
#     # Get today's date
#     curr_date = date.today()
    
#     # Calculate the difference in days
#     age_days = (curr_date - birth1).days
    
#     # Convert the difference from days to years (365.25 days per year)
#     age_years = age_days // 365.25
    
#     return int(age_years)

# print(find_age("1976-11-03"))



#---hands---on-2----------#

#--1--print primes less than 100 using for and while loop
# for i in range(2,101):
#     flag=0
#     if i==2:
#         print(2,end=" ")
#     else:
#         for j in range(2,i):
#             if i%j==0:
#                 flag=1
#                 break
#         if flag==0:
#             print(i,end=" ")

# i=2
# while i<=100:
#     flag=0
#     if i==2:
#         print(i,end=" ")
#     else:
#         j=2
#         while i>j:
#             if i%j==0:
#                 flag=1
#                 break
#             j+=1
#         if flag==0:
#             print(i,end=" ")
#     i+=1


#---2---check number +/-/0
# num=int(input("enter a number: "))
# if num==0:
#     print("it is zero")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is positive")

#---3---prg to take sen as ip and find no.of words
# sen=input("enter a sentence: ")
# c=0
# for i in sen.split(" "):
#     c+=1
# print(f"total words in sentence is {c}")

#---4---prg to create first 10 even numbers
# c,i=1,2
# while c<=10:
#     print(i,end=" ")
#     i+=2
#     c+=1

#---5--prg to swap variables
# a,b=4,5
# b,a=a,b
# print(a," ",b)

#---6---prg takes temp in celsius convert to f
# cel=int(input("enter temparature in celsius: "))
# faren=(cel*(9/5))+32
# print(f"the temparature in farenheit is {faren}")

#---7--prg takes minutes convert to hours and minutes
# minu=int(input("enter no.of minutes to convert to hours: "))
# hr=minu//60
# minuuu=minu%60
# print(f"the converted time is {hr} hours and {minuuu} minute/s")

#---8---prg to find max of three values
# a=int(input("enter number 1: "))
# b=int(input("enter number 2: "))
# c=int(input("enter number 3: "))
# if a>b:
#     if a>c:
#         print(f"{a} is largest")
#     else:
#         print(f"{c} is largest")
# elif a<b:
#     if b>c:
#         print(f"{b} is largest")
#     else:
#         print(f"{c} is largest")
