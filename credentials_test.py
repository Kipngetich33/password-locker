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

    def tearDown(self):
        '''
        A method that clears the class properties each time  test has been completed
        specifically in this case the method clears the list_of_credentials
        '''
        Credentials.list_of_credentials=[]

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

    def test_save_multiple_credential(self):
        '''
        Functions checks if the save can add several credentials 
        to the list of credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Felix","twitter","Felback24")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),2) 

    def test_delete_credential(self):
        '''
        Function that tests if a user can delete a credential
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Felix","twitter","Felback24")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_find_credential_by_name(self):
        '''
        Function that tests whether a credential can be searched with a
        name and credial returned
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Felix","twitter","Felback24")
        test_credential.save_credentials()

        found_credential = Credentials.find_credentials_by_name("Felix")
        self.assertEqual(found_credential.credential_name,test_credential.credential_name)

    def test_credential_exists(self):
        '''
        Function that determine whether a credential exists
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Felix","twitter","Felback24")
        test_credential.save_credentials()

        credential_exist = Credentials.credential_exists("Felix")
        self.assertTrue(credential_exist)
       

    def test_display_credentials(self):
        '''
        Function that tests if the application can display all credentials
        '''
        self.assertEqual(Credentials.display_all_credentials(), Credentials.list_of_credentials)




if __name__ == '__main__':
    unittest.main()
