#input your choice password and confirm the password
Password=input("Enter your choice password: ")
Confirm_password=input("Confirm password: ")
#A conditional statement
if Password==Confirm_password:
    print("Password has been accepted")

elif Password!=Confirm_password:
      print("Password has not been accepted")
      print("Password doesn't match....TRY AGAIN!!")
#A loop to ensure username can still be set after being failed
while Password!=Confirm_password:
       Password= input("Enter your choice password: ")
       Confirm_password = input("confirm password: ")
print("Done")
print("Proceed to the login page")
#input your choice Username and confirm the Username
Username=input("Enter your personal Username: ")
Confirm_Username=input("Confirm Username: ")
#A conditional statement
if Username==Confirm_Username:
    print("Account created")
elif Username!=Confirm_Username:
      print("Account not created")
      print("Username doesn't match....TRY AGAIN!!")
#A loop to ensure password can still be set after being failed
while Username!=Confirm_Username:
       Username= input("Enter your personal Username: ")
       Confirm_Username= input("Confirm Username: ")

print("DONE")
print("CONTINUE")














