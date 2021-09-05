#!/usr/bin/env python3.8
from Locker import User

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