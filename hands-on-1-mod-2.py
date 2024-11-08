#1----funtion return largest prime number less than n
def preceded_prime(n):
    def is_prime(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    lt=[]
    for i in range(2,n):
        if is_prime(i):
            lt.append(i)
    return lt[-1]
# n=int(input("enter a number: "))
# print(preceded_prime(n))

#2----write function that gives intersection of lists
def findcommon(lt1,lt2):
    lt1=set(lt1)
    lt2=set(lt2)
    lt3=[]
    for i in lt1:
        if i in lt2:
            lt3.append(i)
    return lt3
# print(findcommon([1,2,3,4,5,4],[1,2,3,4,6,7,8,8]))

#3----leapyear or not
def is_leap(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    return False

#4----function positivesum()
def positivesum(lt):
    return sum(i for i in lt if i>0)
# print(positivesum([1,2,3,-1,-3,10]))
#5----function listsquare()
def listsquare(lt):
    return list(i*i for i in lt)
# print(listsquare([1,3,4,5,10]))
#6----function to calculate area of rectangle
def rec_area(l,b):
    return l*b
#7----function with lambda for area calculation
area_rec=lambda l,b:l*b
# print(area_rec(12,13))