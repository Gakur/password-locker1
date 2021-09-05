import random
import string

class User :
    """
     Class that generates new instances of User's

    """

    user_List = [] #empty user list
    def __init__(self, username, password) -> None:

        """
        This method defines the properties required for a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        This a method that saves a new user instance into the user List.
        """
        User.user_list.append(self)
    
