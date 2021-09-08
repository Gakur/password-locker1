# PASSWORD-LOCKER   
## Author

[Peter Gakure](https://github.com/Gakur)

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## User Stories
As a user, I would like to.... :
* Create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do not want anymore.


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.8.10

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Gakur/password-locker1.git```

* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x locker_deails.py
        $ ./locker_details.py
* To run test for the application
        $ python3 locker_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./locker_details.py```|Hello Welcome to your Accounts Password Locker Application... <br>* CNA ---  Create New Account * LI ---  Log In if you already Have An Account |
|Select  CNA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CNC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```grp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DL```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exist|
|Exit the application| Enter ```EX```| The application exits|

## Technologies Used

* python3.6

## Known Bugs
* There are no known bugs currently.

## Contact Information 

If you have any question or contributions, please email me at [petergakure97@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Peter Gakure**
