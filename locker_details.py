#!/usr/bin/env python3.8
from Locker import User
from Locker import Credentials

def function():
	print("               ____                         _____  _                               ")
	print("              |  _ \                       / ____|| |                              ")
	print("              | |_) )  ____  ___   ___    / ____  | |__    _____  _ _  ____        ")
	print("              |  __/  / _  |/ __  / __    \___  \ |  __)  /  _  \| '_|/ __ \       ")
	print("              | |    / (_| |\__ \ \__ \    ___  / | |___ (  (_)  ) | |  ___/       ")
	print("              |_|    \_____| ___/  ___/   |____/  |_____) \_____/|_|  \____        ")
function()

def create_new_user(username,password):
    '''
    This is a Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_new_user(user):
    '''
    This function saves a new user
    '''
    user.save_new_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(Account,userName,passWord):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(Account,userName,passWord)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password

def passwordLocker():
    print("Hello Welcome to your Accounts Password Locker Application...\n Please enter one of the following to proceed.\n CNA ---  Create New Account  \n LI ---  Log In if you already Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "cna":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own password:\n GRP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'grp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_new_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your new account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Please enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Application")  
            print('\n')
    while True:
        print("Use these short codes:\n CNC - Create a new credential \n DC - Display Existing Credentials \n FC - Find a credential \n GRP - Generate A randomn password \n DL - Delete a credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cnc":
            print("Create a New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own password if you already have an account:\n GRP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'grp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} have been created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here is your list of accounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.Account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..Use CC to create a new credential........")
        elif short_code == "fc":
            print("Enter the Credentials Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.Account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.passWord}")
                print('-' * 50)
            else:
                print("That Credential does not exist. Enter CC to create it.")
                print('\n')
        elif short_code == "dl":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.Account} have been deleted successfully!!!")
                print('\n')
            else:
                print("Sorry !!! The Credential you want to delete does not exist")

        elif short_code == 'grp':

            password = generate_Password()
            print(f" {password} Has been generated succesfully. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using Passwords Locker Application.. Have a nice day and See you next time!")
            break
        else:
            print("Sorry... invalid input...Kindly check and try again")

if __name__ == '__main__':
    passwordLocker()   