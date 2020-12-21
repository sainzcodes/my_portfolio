'''Password Generator by Santiago Sainz'''

#import modules
import random

#list of characthers that will be used to create the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

#loop for user's input
#request amount of passwords and length


while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for _ in range (password_count):
        password = ""


        #the password length has already been assigned
        for _ in range (password_len):

                #the password will grab a random character from the char list
                password_char = random.choice(chars)
                password      = password + password_char 

                #send a message to the user with the new password
                #return the newly created password to the user  
        print ("Here is your password : ", password )
    print ("Remember to never reveal your password to others, Use different passwords for different accounts,length trumps complexity. Complexity still counts.")
    print ("Test your password security","https://www.security.org/how-secure-is-my-password/")



