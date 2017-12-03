class Credentials:
    '''
    This is class that stores all the credentils of each user
    and hence allows the user to access the information once they are logged in
    '''
    def __init__ (self,user_name, credential_name , credential__password):
        self.user_name = user_name
        self.credential_name =credential_name
        self.credential__password =credential__password

    list_of_credentials=[]  #this is an empty list that will hold all the information for each user

    # def create_credentials(u_name,c_name,c_password):

        
    