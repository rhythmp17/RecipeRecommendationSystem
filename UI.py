import main
from maskpass import askpass
import os
def checkForUsername(uname):
    with open('UserData.txt','r') as file:
        for line in file:
            data = line.split(',')
            if data[1] == uname:
                pw = data[2][:-1]
                return True,pw
    return False,""
def Login():
    print("--------------LOGIN---------------")
    uname = ""
    user_pass = ""
    # correct_pass = ""
    while True:
        uname = input("Enter Your Username : ")
        user_pass = askpass("Enter Your Password : ",mask = ".")
        flag,pw = checkForUsername(uname)
        if flag == True:
            if user_pass == pw:
                print("Login Successfull!!")
                break
            else:
                print("Password Incorrect!")
        else :
            print("Username Not Found !!")
            print("Do you have an account ? [Y,n]")
            res = input().lower()
            if res == "n":
                Signup()
        
    pass
def Signup():
    print("--------------SIGNUP---------------")
    print("Enter Your Name: ")
    name = str(input())
    print("Enter Your username: ")
    username = input()
    while True:
        password = askpass("Set Your Password : ",mask = '.')
        conf_pass = askpass("Confirm Password : ",mask = '.')
        if conf_pass == password:
            print("Account Created Successfully!!")
            break
    
    with open("UserData.txt",'a+') as file:
        file.write(name + "," + username + "," + password + '\n')
    print("Do you want to Login now ?? [Y,n]")
    re = input().lower()
    if re == "n":
        return
    elif re == "y":
        Login()
    pass
print("Welcome to RRS!")
print("Do you have an account? [Y/n] : ")
while True:
    response = str(input()).lower()
    print(response)
    if(response == "y"):
        Login()
        break
    elif(response == "n"):
        Signup()
        break
    else:
        print("Type 'Y' or 'N'!!")

print("Enter Your Ingridients Space Separated :")
lst = input().split(" ")
# print(type(ingredients))

df = main.recommend_recipe(lst)
print(df["recipies"])
full_data = main.recipes_data
# print(full_data.iloc[21,:])
print("Enter the ID of the recipe, you want to make.")
id = int(input())
print("Description : ")
print(full_data.iloc[id,3])
print("-----------------------------------------------------------------------------------------------------")
print("Ingredients : ")
print(full_data.iloc[id,6])
print("Directions : ")
print(full_data.iloc[id,7])
print("-----------------------------------------------------------------------------------------------------")