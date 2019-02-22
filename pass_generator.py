# simple password generator 
    
import random
import string

lenstr = int(input("Enter Length of String: "))
N = int(input("Enter no of password combo need to generated: "))
q1 = input("do you need to save output in file[Y/N]: ")

# password generate function
def pwd(N,lenstr,q1):
    pwd = ""
    count = 0
    
    while count != lenstr:        #takes random variable one by one and add to string until reaches lenstr

        upper = [random.choice(string.ascii_uppercase)]  #ABCDEFGHIJKLMNOPQRSTUVWXYZ
        lower = [random.choice(string.ascii_lowercase)]  #abcdefghijklmnopqrstuvwxyz
        num = [random.choice(string.digits)]             #0123456789
        symbol = [random.choice(string.punctuation)]     # #@!$%^&*()-+[]{}~,./\?<>;:_=    #without whitespace and quotes
        everything = upper + lower + num + symbol

        pwd += random.choice(everything)
        count += 1
        continue

    if count == lenstr:  #count reaches length
        print (pwd)

    if q1 == 'Y' or q1 == 'y':                      #if yes store the passwords to file
        with open('pass.txt','a') as file_:         #appends text each time
            print(pwd, file = file_)

# result
print("\nPasswords are:\n"+"-"*100)
for i in range(0,N):
    pwd(N,lenstr,q1)

print("-"*100)

if q1 == 'Y' or q1 == 'y':
    print("passwords are stored in pass.txt")  #notify user
