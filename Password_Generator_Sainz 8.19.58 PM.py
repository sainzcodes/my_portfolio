#Import the module in order to use it on the program
import random

#This characters will be used to generate the new password
#The more character types, the more secure the password will be
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

#This loop while request information from the user
#The program will gather what length the password needs to be
#As well as how many passwords need to be created for the use


while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for _ in range (password_count):
        password = ""


        #The password length will be assigned by the user
        #It will run from 0 to the value assigned to password_len
        for _ in range (password_len):

                #The password will grab a random character from the char list
                #We use the module random to assign the task
                #The password will now be assigned to the newly generated characters
                password_char = random.choice(chars)
                password      = password + password_char 

                #Send a message to the user with the new password
                #Return the newly created password to the user  
        print ("Here is your password : ", password )
    print ("Remember to never reveal your password to others, Use different passwords for different accounts,length trumps complexity. Complexity still counts.")
    print ("Test your password security","https://www.security.org/how-secure-is-my-password/")



