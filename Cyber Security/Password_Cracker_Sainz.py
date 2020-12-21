'''Password Cracker by Santiago Sainz'''

# import modules
import itertools
import time


#declare the paramaters for the program
#socket.AF selects IPV4
#socket.SOCL_STREAM selects tcp
#processing duration:> 5 minutes
#Returns the number of attempts and distance
def tryPassword(passwordSet, stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance)


password = input("Password >")

#list of characthers that will be used to crack the password
#return the password, number of attempts, and time to the user 
stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
tries, timeAmount = tryPassword(password, stringType)
print("Sainz's BFPC cracked the password %s in %s tries and %s seconds!" % (password, tries, timeAmount))
