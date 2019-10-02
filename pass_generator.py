'''
    A simple python script to generate passwords. The passwords are generated from the 
    passwordGenerator method. The generated passwords are stored/not stored in a file
    depending on the user's preference
'''

import random
import string

'''
    Method name:
        passwordGenerator(len_of_password, save)
    Arguements:
        len_of_password (int): The length of the password to be generated.
        save (char): A char arguement which either contains Y/N depending on whether the 
                    passwords need to be saved in a file
    Returns:
        None: When the method finishes executing the passwords are saved in a file.
'''

def passwordGenerator(len_of_password, save):
    
    password = ""
    count = 0
    
    while count != len_of_password:  # count keeps track of the number of characters in the password
        upper = [random.choice(string.ascii_uppercase)]  # all upper case alphabets
        lower = [random.choice(string.ascii_lowercase)]  # all lower case alphabets
        num = [random.choice(string.digits)]             # all digits
        symbol = [random.choice(string.punctuation)]     # all special characters except spaces
        everything = upper + lower + num + symbol

        password += random.choice(everything)
        count += 1
        continue

    if save == 'y':                      # if yes store the passwords to file
        with open('pass.txt','a') as file_:         # append every password to the file
            print(password, file = file_)

if __name__ == "__main__":
    len_of_password = int(input("Enter length of the password needed: "))
    number_of_passwords = int(input("Enter the number of passwords needed to be generated: "))
    save = input("Do you want the passwords to be saved in an output file[Y/N]: ")

    save = str.lower(save)

    for i in range(0,number_of_passwords):
        passwordGenerator(len_of_password,save)

    if save == 'y':
        # Notify the user about the file where the passwords are saved
        print("Passwords are stored in pass.txt")
