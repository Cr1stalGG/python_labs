import time, random

password = input("Input the right password: ")

numOfTries = random.randrange(3, 10, 1)

inc_pass = input("Input password: ")
while inc_pass != password:
    for i in range(numOfTries-1):
        print("Incorrect password!!!")
        print(numOfTries-i-1, "tries...")
        inc_pass = input("Input password: ")
        if password == inc_pass:
            break
    if password == inc_pass:
        break
    print("Large amount of incorrect tries... Wait for 3 minutes to continue")
    time.sleep(2)

print("Success")
