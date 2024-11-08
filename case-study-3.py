import json
from datetime import datetime
# ---- Signup function ------
def signup():
    print("==== Customer SignUp ====")
    dic = {}
    uname = input("Enter your name: ")
    dic['uname'] = uname
    pwd = input("Enter your password: ")
    dic['pwd'] = pwd
    sec_ans = input("Enter your favorite color: ")
    dic['sec_ans'] = sec_ans
    dic['balance']=0
    dic['fund']=0

    # Load existing data if available
    try:
        with open("case-study-3.txt", "r") as file:
            info = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        info = []

    info.append(dic)

    # Write updated data back to file
    with open("case-study-3.txt", 'w') as f:
        json.dump(info, f, indent=4)
    print("Sign Up confirmed!!")
    print("==================")

# ----- Signin function -----
def signin():
    start_hour = 9
    end_hour = 17
    working_days = range(0, 5) 
    now = datetime.now()
    current_hour = now.hour
    current_day = now.weekday()
    
    print("===== Sign In =====")
    name = input("Enter your name: ")
    passw = input("Enter your password: ")
    fl = 0

    try:
        with open("case-study-3.txt", 'r') as file:
            info = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        info = []
    
    def save_info():
        with open("case-study-3.txt", 'w') as f:
            json.dump(info, f, indent=4)


    def show_balance(sname):
        for i in info:
            if i['uname']==sname:
                return i['balance']
            
    def deposit(name,amt):
        for i in info:
            if i['uname']==name and amt<=50000:
                i['balance']+=(amt-500)
                i['fund']+=500
                save_info()
                return 1
        return 0

    def withdraw(name,withamt):
        for i in info:
            if i['uname']==name:
                i['balance']-=withamt
                save_info()
                return 1
        return 0
    def fund_transfer(fname,famt):
        for i in info:
            if i['uname']==fname:
                i['balance']+=famt
                save_info()
                return 1
        return 0

    for i in info:
        if i['uname'] == name and i['pwd'] == passw:
            fl = 1
            print("Successful login")
            print("==================")
            while True:
                print("Customer Menu")
                print("--------------")
                print("1) Show Balance\n2) Deposit\n3) Withdraw\n4) Fund Transfer\n5) Exit")
                ch=int(input("Enter your choice: "))
                if ch==1:
                    print(show_balance(name))
                elif ch==2:
                    if current_day in working_days and start_hour <= current_hour < end_hour:
                        amt=int(input("enter the amount you want to deposit: "))
                        resd=deposit(name,amt)
                        if resd==1:
                            print("Deposit success")
                        else:
                            print("Amount should not be more than 50k")
                    else:
                        print("Desposit can be made only in work hours and on weekdays")
                elif ch==3:
                    if current_day in working_days and start_hour <= current_hour < end_hour:
                        withamt=int(input("enter the amt to be withdrawn: "))
                        if i['fund']<=500:
                            print("no sufficient funds")
                        else:
                            resw=withdraw(name,withamt)
                            if resw==1:
                                print("withdraw successfull")
                            else:
                                print("withdraw failed!!")
                    else:
                        print("Withdraws can be made only in work hours and on weekdays")
                elif ch==4:
                    fname=input("enter the name of customer to transfer your funds: ")
                    famt=int(input("enter the amt to get transfferd: "))
                    if i['balance']>=famt:
                        i['balance']-=famt
                        resf=fund_transfer(fname,famt)
                        if resf==1:
                            print("Funds are transffered")
                        else:
                            print("Problem in funds transfer!!")
                    else:
                        print("you balance is low")
                elif ch==5:
                    print("Exiting Progeam")
                    exit()
                else:
                    print("Invalid choice. please try again.")


    if fl == 0:
        print("User name or password is incorrect")
        want = input("Want to Sign Up? (y/n): ").lower()
        if want == 'y':
            signup()
        else:
            exit()


#driver code
while True:
    print("Main Menu: ")
    print("==============")
    print("1) Customer SignUp\n2) Customer SignIn\n3) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        signup()
    elif choice == 2:
        signin()
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")