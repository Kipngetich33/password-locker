import unittest # this line imports the unittest module
from user import User # this lines imports the class User from user.py

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for the user
     class behaviours
     Args:
        unnitest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        this is the set up method that should run before each test case
        '''
        self.new_user= User("Vincent","Empharse")

    def test_init(self):
        '''
        this function tests an a user object is properly initialized
        '''
        self.assertEqual(self.new_user.name,"Vincent")
        self.assertEqual(self.new_user.password,"Empharse")

if __name__ == '__main__':
    unittest.main()

     

