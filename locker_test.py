import unittest  # Importing the unittest module
from Locker import User  # Importing the User class

class TestClass (unittest.TestCase) :
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