import random
import string

class User :
    """
     Class that generates new instances of User's

    """

    user_List = [] #empty user list
    def __init__(self, username, password):

        """
        This method defines the properties required for a user.

        """
        self.username = username
        self.password = password

    def save_new_user(self):
        """
        This a method that saves a new user instance into the user List.
        
        """
        User.user_List.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_List

    def delete_user(self):
        '''
        delete_user method deletes a saved user's account from the list
        '''
        User.user_List.remove(self)   
    
class Credentials :
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_List = []

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user exists in the user_list or not
        """
        a_user = ""
        for user in User.user_List:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user

    def __init__(self,Account,userName, passWord):
        """
        method that defines user credentials to be stored
        """
        self.Account = Account
        self.userName = userName
        self.passWord = passWord
    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_List.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_List
        """
        Credentials.credentials_List.remove(self)
    
    @classmethod
    def find_credential(cls, Account):
        """
        Method that takes in an account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_List:
            if credential.Account == Account:
                return credential

    @classmethod
    def if_credential_exist(cls, Account):
        """
        This Method checks if a credential exists from the credential list and returns true or false depending if the credential exists or not.
        """
        for credential in cls.credentials_List:
            if credential.Account == Account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        This Method returns all items present in the credentials list

        """
        return cls.credentials_List

    def generatePassword(stringLength=8):
        """
        Generate a random password string that consists of letters, digits and special characters
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))