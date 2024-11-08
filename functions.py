#---task-1-----#
#-----functions without argument-----#
#1--funtion dispalys welcome msg
def welcome_fun():
    print("Hello, welcome to functions")

#2---function that draws line
def draw_line():
    print("----------------------------")

#3---function that dispaly msg based on time
import datetime
def time_fun():
    curr_datetime=datetime.datetime.now()
    hourtime=curr_datetime.hour
    if 0<=hourtime<=12:
        print("Good Morning!")
    elif 12<hourtime<=16:
        print("Good Afternoon!")
    else:
        print("Good Evening!")

#4---funtion to dispaly capital alphabets
def capitalalpha():
    for i in range(97,123):
        print(chr(i).capitalize(),end=" ")

#5---function to dispaly small alphabets
def smallalpha():
    for i in range(65,91):
        print(chr(i).lower(),end=" ")


#----task-2------#
#----function with arguments
#1---function with 3 sub arguments dispaly tottal,avg,result grade
def examresult(sub1,sub2,sub3):
    total=sub1+sub2+sub3
    avg=total/3
    print(f"total is {total} and avg is {avg}")
    if 80<=avg<100:
        print("A grade")
    elif 60<=avg<80:
        print("B grade")
    elif 50<=avg<60:
        print("C grade")
    else:
        print("Fail")

#2---function takes name as argument dispaly wishes
def name_wish(name):
    print(f"welcome!! {name}")

#3---function take number and diaplay multipliaction table
def multiplication(num):
    for i in range(1,11):
        print(f"{num} x {i}={num*i}")

#4---function take number and display that many fibonacci series
def fibonacci(n):
    if n==1:
        print("0")
    elif n==2:
        print("0 1")
    else:
        print("0 1",end=" ")
        n1,n2=0,1
        for i in range(n-2):
            temp=n1+n2
            print(temp,end=' ')
            n1=n2
            n2=temp

#5---function that takes single character dispaly if it is 
    #small/caps/space/digit/special char
# def define_input(ele):
#     lt=['!','@','#','$','%','^','&','*','(',')','[',']','{','}','/']
#     if isinstance(ele,int):
#         print("input is digit")
#     elif isinstance(ele,str):
#         if ele.isalpha():
#             if ele.isupper():
#                 print("input is capital")
#             else:
#                 print("input is small")
#         elif ele==' ':
#             print("input is space")
#         elif ele in lt:
#             print("input is special char")
#     else:
#         print("no type")
# define_input(100)

#6---function dispaly primes b/w start and end
# def primes_between(start,end):
#     for i in range(start,end+1):
#         if i==2:
#             print(i,end=" ")
#         else:
#             fl=0
#             for j in range(2,i):
#                 if i%j==0:
#                     fl=1
#                     break
#             if fl==0:
#                 print(i,end=" ")


#-----task-3----------
#-----function returning values
#1---function takes number and return square
def square_num(num):
    return num**2

# print(square_num(5))

#2---return sum of two nums
def add_num(a,b):
    return a+b

#3---return max of two nums
def max_of_nums(a,b):
    if a>b:
        return a
    return b
# print(max_of_nums(10,1000))

#4---return min of two nums
def min_of_nums(a,b):
    if a<b:
        return a
    return b


#---------task-4----------
#---------function returning values-----
#1---fun takes int return count of digits
def count_of_int(num):
    return len(str(num))
# print(count_of_int(100))

#2---fun takes int return count of zero digits
def count_of_zeros(num):
    return str(num).count('0')
# print(count_of_zeros(10000))

#3---fun takes int return count of even digits
def count_of_even(num):
    c=0
    for i in str(num):
        if int(i)%2==0:
            c+=1
    return c
# print(count_of_even(1234567890))

#4---fun takes int retun sum of digits
def sum_of_digits(num):
    sum=0
    for i in str(num):
        sum+=int(i)
    return sum

#5---fun takes int return reverse int
def rev_int(num):
    return int((str(num))[::-1])
# print(rev_int(12345))


#-----------task-5---------#
#----------function returning boolean------
#1-----fun takes int and return if leap
def leap_or_not(num):
    if (num%4==0 and num%100!=0) or num%400==0:
        return True
    return False
# print(leap_or_not(2024))

#2---check perfect or not
def is_perfect(num):
    sum=1
    for i in range(2,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    return False
# print(is_perfect(10))

#3---palindrome or not
def is_palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    return False
# print(is_palindrome(1551))

#4---prime or not
def is_prime(num):
    if num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
# print(is_prime(78))

#---armstrong or not
def is_armstrong(num):
    n,sum=num,0
    for _ in range(3):
        a=n%10
        sum+=a**3
        n//=10
    if num==sum:
        return True
    return False
# print(is_armstrong(150))

