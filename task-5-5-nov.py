# 1 # generate current bill
    # input is presnt and last month meter readings
    # bu=pmr-lmr
# bu  ur
# <200 1.5
# <400 2.75
# <500 3.45
# >=500 7
    #amount=bu*ur

pmr=int(input("enter present meter reading: "))
lmr=int(input("enter last month meter reading: "))
bu=pmr-lmr
if bu>=500:
    print("current bill amount is: ",(bu*7))
elif 400<=bu<500:
    print("current bill amount is: ",(bu*3.45))
elif 200<=bu<400:
    print("current bill amount is: ",(bu*2.75))
else:
    print("current bill amount is: ",(bu*1.5))