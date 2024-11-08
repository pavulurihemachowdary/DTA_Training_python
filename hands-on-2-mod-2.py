#prg to accept 2 numbers raise error if divides by zero
def error_handling(a,b):
    try:
        res=a/b
        return res
    except ZeroDivisionError:
        print("b value can not be zero")
        exit()
        
print(error_handling(2,2))