#-----creating file with write mode

# with open('info.txt','w') as file:
#     file.write("My name is hema\nI am writing to info.txt\nthis is the last line")

#-----reading from file calculating small,capital,spaces,total letters
# with open('info.txt','r') as file:
#     lines=file.readlines()
#     sum,caps,small,space=0,0,0,0
#     for line in lines:
#         for i in line:
#             if i.isupper():
#                 caps+=1
#             elif i.islower():
#                 small+=1
#             elif i.isspace():
#                 space+=1
#         sum+=len(line)
        
# print("total length is ",sum)
# print("total capitals is ",caps)
# print("total smalls is ",small)
# print("total spaces is ",space)

#--------hands-on-3--------------
# with open('test.txt','w+') as file:
#     file.write("A girl is playing\nShe is in a playground\n")
#     file.write("The sky above is pink\nA balloon is in the sky\n")
#     file.write("The balloon is blue")
#     file.seek(0)
#     lines=file.readlines()
#     tot,the=0,0
#     for line in lines:
#         word=line.split()
#         for i in word:
#             if i.lower()=='a' or i=='an':
#                 tot+=1
#             elif i.lower()=='the':
#                 the+=1
#     f=open("result.txt",'a')
#     f.write(f"total articles(a,an,the):{tot+the}\n")
#     f.write(f"total (the) articles:{the}")


#---------hands-on-4-------------
#prg to find product of a,b if a*b<=1000 else a+b
# def prodprg(a,b):
#     if a*b<=1000:
#         return a*b
#     return a+b
# print(prodprg(40,50))


#--------hands-on-5---operate numbers-------
# def operate_numbers(a,b,s):
#     if s=='+':
#         return a+b
#     elif s=='-':
#         return a-b
#     elif s=='*':
#         return a*b
#     elif s=='/':
#         return a/b
#     elif s=='//':
#         return a//b
#     elif s=='%':
#         return a%b
#     elif s=='**':
#         return a**b
#     return 0
# print(operate_numbers(10,2,'-'))

#--------hands-on-6----calculate_tax-----
# def calculate_tax(sal):
#     if sal<3*(10**5):
#         return 0
#     elif (3*(10**5))<=sal<(6*(10**5)):
#         return sal-(sal*0.05)
#     elif (6*(10**5))<=sal<(9*(10**5)):
#         return sal-(sal*0.10)
#     elif (9*(10**5))<=sal<(12*(10**5)):
#         return sal-(sal*0.15)
#     elif (12*(10**5))<=sal<(15*(10**5)):
#         return sal-(sal*0.20)
#     elif sal>(15*(10**5)):
#         return sal-(sal*0.3)
# print(calculate_tax(1000000))

#----------hands-on-7-----cipher_sentence--
# from itertools import zip_longest
# def cipher_sentence(msg):
#     vowels=['a','e','i','o','u']
#     lt=msg.lower().split()
#     result=''
#     for i in lt:
#         if len(i)==2:
#             result+=i[::-1]+' '
#             continue
#         if len(i)==1:
#             result+=i+' '
#             continue
#         odd,ev,ec=[],[],[]
#         res=''
#         for j in i:
#             if (i.index(j)+1)%2!=0:
#                 odd.append(j)

#             else:
#                 if j in vowels:
#                     ev.append(j)
#                 else:
#                     ec.append(j)
#         ev.sort()
#         ec.sort()
#         odd=odd[::-1]
#         even=ec+ev
#         res+=''.join((a or ' ')+(b or ' ') for a,b in zip_longest(odd,even))
#         result+=res+' '
#     return result
# print(cipher_sentence('how are you doing ?'))

#----------hands-on-8-price_dictionary-------
# def price_dictionary(prices):
#     new_dict={}
#     for key,val in prices.items():
#         if val>200:
#             new_dict[key]=val
#     return new_dict
# prices={'apple':45,'mango':800,'orange':250,'banana':100}
# print(price_dictionary(prices))



