Attempts = 0
Accepted = False

while Accepted == False:
    while Attempts < 3:
        Uname = input("Please enter your username: ")
        Pword = input("Please enter your password: ")
        if Uname == "Admin" and Pword == "Password":
            print("Welcome")
            Accepted = True
            break
        else:
            Attempts = Attempts + 1
            if Attempts == 3:
                Accepted = True
                print("System Locked")
            else:
                print("Try Again")
