# •	Password Generator – User chooses length and options (letters, numbers, symbols), program outputs random password.
import random
import string
def password_generator(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*"
    password = []
    
    print("\nEnter your choices: ")
    user_letter = input("Do you want letter?(Y/N): ").lower() == 'y'
    user_digit = input("Do you want digit?(Y/N): ").lower() == 'y'
    user_symbols = input("Do you want symbols?(Y/N): ").lower() == 'y'
    
    temp = ""
    if user_letter:
        temp += letters
    if user_digit:
        temp += digits
    if user_symbols:
        temp += symbols
        
    for i in range(length):
        var = random.choice(temp)
        password.append(var)
    return "".join(password)
   
username = input("Hello, please enter your name: ")
length = int(input(f"{username}, please enter the length of your password: "))
password =  password_generator(length)
print(f"\n{username}, your random password is: {password}")

input("Press Enter to exit :)")