# Case Study 1 - Objective Question Paper
import json

def exam_paper():
    print("----Objective with 5 MCQs----")
    questions = [
        {'question': 'Sun rises in the? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'A'},
        {'question': 'Sun sets in the? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'B'},
        {'question': 'Opposite of North? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'D'},
        {'question': 'Opposite of South? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'C'},
        {'question': 'USA lies to ____ of world? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'B'},
        {'question': 'Sun rises in the? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'A'},
        {'question': 'Sun sets in the? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'B'},
        {'question': 'Opposite of North? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'D'},
        {'question': 'Opposite of South? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'C'},
        {'question': 'USA lies to ____ of world? ',
            'options': ['A: East', 'B: West', 'C: North', 'D: South'],
            'answer': 'B'},
    ]
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for j in q['options']:
            print(j)
        user_ans = input("Type any one option (A/B/C/D): ").upper()
        if user_ans == q['answer']:
            score += 1
    return score

# ---- Signup function ------
def signup():
    print("==== User SignUp ====")
    dic = {}
    uname = input("Enter your name: ")
    dic['uname'] = uname
    pwd = input("Enter your password: ")
    dic['pwd'] = pwd
    sec_ans = input("Enter your favorite color: ")
    dic['sec_ans'] = sec_ans

    # Load existing data if available
    try:
        with open("case-study-1.txt", "r") as file:
            info = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        info = []

    info.append(dic)

    # Write updated data back to file
    with open("case-study-1.txt", 'w') as f:
        json.dump(info, f, indent=4)
    print("Sign Up confirmed!!")
    print("==================")

# ----- Signin function -----
def signin():
    print("===== Sign In =====")
    name = input("Enter your name: ")
    passw = input("Enter your password: ")
    fl = 0

    try:
        with open("case-study-1.txt", 'r') as file:
            info = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        info = []

    for i in info:
        if i['uname'] == name and i['pwd'] == passw:
            fl = 1
            print("Successful login")
            print("==================")
            res = input("Want to write the test (y/n): ").lower()
            if res == 'y':
                print("====== MCQ Question Paper =======")
                sc = exam_paper()
                print(f"Your score is:{sc}/10")
                print("Correct options are:")
                lt = ['A', 'B', 'D', 'C', 'B','A','B','D','C','B']
                for i, j in enumerate(lt, 1):
                    print(f"{i}: {j}")
            else:
                exit()
            break

    if fl == 0:
        print("User name or password is incorrect")
        want = input("Want to Sign Up? (y/n): ").lower()
        if want == 'y':
            signup()
        else:
            exit()

# ----- Driver Code -----
while True:
    print("Main Menu: ")
    print("==============")
    print("1) User SignUp\n2) User SignIn\n3) Exit")
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
