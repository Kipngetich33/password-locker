class User:
    """ This is a class that helps in generating instances of a user
    """
    def __init__(self,name,password):
        
        """ the init method helps in defining properties of our objects"""
        self.name= name
        self.password= password

    list_of_users=[] #this is an empty list that will store the users

    def save_user(self):
        '''
        This function appends the object user to the list_of_users
        '''
        self.list_of_users.append(self)
    def delete_user(self):
        '''
        This function deletes the passed object from the contact list
        '''
        User.list_of_users.remove(self)

    @classmethod
    def find_user_by_name(cls,name):
        '''
        A method that finds a user using the 
        name of the user and return that user
        '''
        for user in cls.list_of_users:
            if user.name == name:
                return user

    @classmethod
    def user_exists(cls,name):
        '''
        A method that determines if a user exists using the 
        name of the user and returns an boolean
        '''
        for user in cls.list_of_users:
            if user.name == name:
                return True
        return False
    @classmethod
    def display_all_users(cls):
        '''
        A method that returns a list of all users
        '''
        return cls.list_of_users
        
    
