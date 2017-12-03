from credetials import Credentials
import unittest

class TestCredentials( unittest.TestCase ):
    '''
    Class test defines the test for all the behaviours of credentials
    Args:
        unnitest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        A method that should be run before each test case
        '''
        self.new_credential = Credentials("Vincent","facebook","poheri333")

    def test_init(self):
        '''
        A method that checks whether each  credential 
        is properly instanciated
        '''
        self.assertEqual(self.new_credential.user_name,"Vincent")
        self.assertEqual(self.new_credential.credential_name,"facebook")
        self.assertEqual(self.new_credential.credential_password,"poheri333")

    def test_save_credentials(self):
        '''
        A method that determines whether the save function adds
        credentials to the list of credentials
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)
        

if __name__ == '__main__':
    unittest.main()
