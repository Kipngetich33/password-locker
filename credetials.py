class Credentials:
    '''
    This is class that stores all the credentils of each user
    and hence allows the user to access the information once they are logged in
    '''
    def __init__ (self,user_name, credential_name , credential__password):
        self.user_name = user_name
        self.credential_name =credential_name
        self.credential_password =credential__password

    list_of_credentials = []  #this is an empty list that will hold all the information for each user

    def save_credentials(self):
        '''
        This functions appends each new credential to the list of credetials
        '''
        self.list_of_credentials.append(self)
        
    def delete_credentials(self):
        '''
        this method deletes the selected credential from the list of credentials
        '''
        Credentials.list_of_credentials.remove(self)

    @classmethod
    def find_credentials_by_name(cls,name):
        for credential in cls.list_of_credentials:
            if credential.user_name == name:
                return credential

    @classmethod
    def credential_exists(cls,name):
        for credential in cls.list_of_credentials:
            if credential.user_name == name:
                return True

    @classmethod
    def display_all_credentials(cls):
        '''
        Function that displays all the saved credentials in the list of credentials
        '''
        return cls.list_of_credentials
    



        
    