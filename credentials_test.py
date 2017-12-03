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

if __name__ == '__main__':
    unittest.main()
