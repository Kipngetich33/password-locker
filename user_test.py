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

    def tearDown(self):
        '''
        cleans up after each test case has run
        '''
        User.list_of_users=[]

    def test_init(self):
        '''
        this function tests an a user object is properly initialized
        '''
        self.assertEqual(self.new_user.name,"Vincent")
        self.assertEqual(self.new_user.password,"Empharse")

    def test_save_user(self):
        '''
        this function tests the save function appends 
        a new user object to the contact list'''
        self.new_user.save_user()# this line calls the save user contact from user.py
        self.assertEqual(len(User.list_of_users),1)

    def test_save_multiple_contacts(self):
        '''
        this function tests if the application can save multiple contats
        '''
        self.new_user.save_user()# this line calls the save user contact from user.py
        test_user= User("test_user","test_user_password")
        test_user.save_user()# this line save the user test_user to the list_of_users
        self.assertEqual(len(User.list_of_users),2)

    def test_delete_user(self):
        '''
        determines whether the app can delete a user from the list of users
        '''
        self.new_user.save_user()
        test_user= User("test_user","test_user_password")
        test_user.save_user()# this line save the user test_user to the list_of_users
        self.new_user.delete_user()# this lines deletes the user
        self.assertEqual(len(User.list_of_users),1)
        

if __name__ == '__main__':
    unittest.main()

     

