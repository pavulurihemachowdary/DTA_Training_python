# 1 # read m,p,c marks find tot and avg 
    # display res as pass for >=35 in each sub
    # also display grade based on avg and res

m=int(input("enter marks for max(100): "))
p=int(input("enter marks for max(100): "))
c=int(input("enter marks for max(100): "))
tot=m+p+c
avg=tot/3
if (m>=35 and p>=35) and c>=35:
    print("PASS")
if tot>=280:
    print("A grade")
elif 220<=tot<=279:
    print("B grade")
elif tot<=200:
    print("C grade")