import unittest  # Importing the unittest module
from Locker import User  # Importing the User class
from Locker import Credentials  #importing the Credentials class

class TestUser (unittest.TestCase) :
    """
    Test class that defines test cases for the User class behaviours.

    unittest.TestCase: TestCase class that helps in creating test cases.
    """
#First test
    def setUp(self):

       """
       Method that runs before each individual test case.
       """
       self.new_user = User("Peter Gakure","Peter120")  # create User object

    def test_init(self):
       """
       test case to chek if the object has been initialized properly
       """
       self.assertEqual(self.new_user.username,"Peter Gakure")
       self.assertEqual(self.new_user.password,"Peter120")

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_List),1)

class TestCredentials(unittest.TestCase) :
    """
    A test class that defines test cases for credentials class

    """ 
    #first test
    def setUp(self):
        """
        Method that runs before each individual credentials test run.

        """
        self.new_credential = Credentials("Gmail","Peter Gakure","Peter120")

    #second test    
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized as expected correctly.
        """
        self.assertEqual(self.new_credential.Account,"Gmail")
        self.assertEqual(self.new_credential.userName,"Peter Gakure")
        self.assertEqual(self.new_credential.passWord,"Peter120")

    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_List),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_List = []

    #third test
    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","peterjnr","Peter@1010") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_List),2)

    #fourth test
    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","peterjnr","Peter@1010")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_List),1)

    #fifth test
    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","peterjnr","Peter@1010") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Twitter")

        self.assertEqual(the_credential.Account,test_credential.Account)

    #sixth test
    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        the_credential = Credentials("Twitter", "Peter Gakure", "Peter@1010")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(credential_is_found)
 
    #seventh test 
    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_List)

if __name__ == "__main__":
    unittest.main()
       