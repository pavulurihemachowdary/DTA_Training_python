#-----example-1--------

# a=input("enter number1: ")
# b=input("enter number2: ")
# try:
#     res=int(a)/int(b)
# except ZeroDivisionError:
#     print("error: division by zero is not allowed")
#     res=None
# except ValueError:
#     print("both must be number")
#     res=None
# else:
#     print("sucessful",res)
# finally:
#     print("this prints all the time")


#-----------example-2--------------
# def get_integer_input():
#     try:
#         userip=input("enter integer: ")
#         number=int(userip)
#     except ValueError:
#         print("invalid input")
#         number=None
#     else:
#         print("input is valid")
#     finally:
#         print("exceuted everytime")
#     return number

# number=get_integer_input()
# if number is not None:
#     print("integer is ",number)


#-----------example-3-------------
# lt=[10,20,30,40,50]
# try:
#     index=int(input("enter an index to get ele from list: "))
#     ele=lt[index]
#     print(f"the ele at {index} is {ele}")
# except IndexError:
#     print("index is out of range")
# except ValueError:
#     print("enter integer")
# except Exception as e:
#     print("unexpected error")
# finally:
#     print("this is finally")


#-----------example-4 keyerror---------
# emp={'id':1001,'name':'raj','job':'trainer','sal':20000}
# try:
#     key=input("enter key to access value from dic: ")
#     val=emp[key]
#     print(f"the value for key {key} is {val}")
# except KeyError:
#     print("not found any key")
# except Exception as e:
#     print("an unexpected error occured")


#-------------example-4 error---------