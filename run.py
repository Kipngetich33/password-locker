#!/usr/bin/env python3.6

from user import User
from credetials import Credentials
import random 

# This part applies to class User

def create_users(name,password):
    '''
    Function that creates a new contact object by calling 
    the class
    '''
    new_run_user= User(name,password)
    return new_run_user

def save_users(user):
    '''
    Function that saves the created user to the list of users
    '''
    user.save_user()

def delete_users(user):
    '''
    Function that deletes a user
    '''
    user.delete_user()

def find_users(name):
    '''
    Functiont that searches for a user using the name of the user 
    and returns the user
    '''
    return  User.find_user_by_name(name)

def check_if_user_exists(name):
    '''
    Function that returns a boolean value based on whether the user 
    being sough exists
    '''
    return User.user_exists(name)

def displaying_all_users():
    '''
    Function displays all the saved users
    '''
    return User.display_all_users()

#This part applies to class Credentials
def create_credential(user_name,credential_name,credential_password):
    '''
    This is a function that generates a new credential 
    by instatiating a new object of the class Credentials
    '''
    new_run_credential = Credentials(user_name,credential_name,credential_password)
    return new_run_credential

def save_credential_run(credential):
    '''
    This functions calls the save_credentials function from class 
    Credential to append a credential to the list of credentials
    '''
    credential.save_credentials()

def delete_credential_run(credential):
    '''
    Function that deletes a credential from the list of credentials
    '''
    credential.delete_credentials()


def main():
    while True:
        # This is the main menu/ while loop
        print("Please use these shortcodes: lg-login, ca- create a user, fu -find user, du- display users  ex- exit")
        short_code0= input()
        if short_code0 == 'lg':
                print("Enter User Name")
                login_user_name= input()
                print("Enter Password")
                login_password = input()

                if check_if_user_exists(login_user_name):
                    print(f"Welcome {login_user_name}")
                    logged_in_user = find_users(login_user_name)

                    if logged_in_user.password == login_password:

                        print(f"{logged_in_user.name} ...........{logged_in_user.password}")
                        print ('-'*10)
                        while True:
                            print("Enter cc- to add a credential ,dc- display credentials, dl -delete credential ex -exit")
                            shortcode3 = input()

                            credential_user_name = logged_in_user.name

                            if shortcode3 == 'cc':

                                while True:
                                    print("use these short codes 1- enter you own password 2 -for system generated password \'ok' -continue , ex- exit ")
                                    short_code5 = input()

                                    if short_code5 == '1':
                                        print(f"welcome {credential_user_name} add a credential") 
                                        print("Enter credential name")
                                        name_of_credential =input()
                                        print("Enter password for the credential")
                                        password_of_credential = input()

                                        save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                        
                                        print("You Credentials")
                                        print ('-'*10)
                                        for credential in Credentials.display_all_credentials():
                                            if credential_user_name == credential.user_name:
                                                print(f"Credential:{credential.credential_name}......Password:{credential.credential_password}")
                                    

                                    elif short_code5 == '2':
                                        print(f"welcome {credential_user_name} add a credential") 
                                        print("Enter credential name")
                                        name_of_credential =input()
                                        print("You Password has been generated")
                                        password_of_credential = random.randint(10000,99000)

                                        save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                        
                                        print("You Credentials")
                                        print ('-'*10)
                                        for credential in Credentials.display_all_credentials():
                                            if credential_user_name == credential.user_name:
                                                print(f"Credential:{credential.credential_name}......Password:{credential.credential_password}")

                                    elif short_code5 == 'ok' or 'ex':
                                        break

                                    else:
                                         print("Invalid Input, please use the provided shortcodes")


                            elif shortcode3 == 'dc':
                                print("You Credentials")
                                print ('-'*10)
                                for credential in Credentials.display_all_credentials():
                                    if credential_user_name == credential.user_name:
                                        print(f"{credential.credential_name}......{credential.credential_password}")

                            elif shortcode3 == 'dl':
                                if Credentials.credential_exists(credential_user_name):
                                    print("Enter Name of Credential to delete")
                                    credential_for_delete = input()

                                    for credential in Credentials.display_all_credentials():
                                        if credential.credential_name == credential_for_delete:
                                            credential.delete_credentials()
                                            print(f"Deleted {credential_for_delete}")
                                            print("\n")

                                        else:
                                            print ('-'*10)
                                            print("The credential does not exist")
        
                                else:
                                    print("You have not added any credentials yet")        

                            elif shortcode3 == 'ex':
                                print("exiting credentials")
                                break

                            else:
                                print("Invalid Choice please use the short codes")
                            
                else:
                   print ('-'*10)
                   print("Wrong user name and password combination")
                   print ('-'*10)


        elif short_code0 == 'ca':
            print ("New User")
            print('-'*10)

            while True:
                print("use these short codes 1- enter you own password 2 -for system generated password \'ok' -continue , ex- exit ")
                short_code4 = input()

                if short_code4 == '1':
                    print ("Enter Your Name")
                    user_name_run2= input()
                    print ("Enter a password")
                    user_password_run2 =input()

                    save_users(create_users(user_name_run2, user_password_run2))
                    print("\n")
                    print (f"New user created") 
                    print('-'*10)
                    print("user ...............password")
                    print(f" name:{user_name_run2}.... Password:{user_password_run2} ")

                    #This part invokes the credentials class
                    print ('-'*10)
                    print("You can now login to add a new credential")
                    print("enter \'ok'\' to continue")
                    print ('-'*10)
                elif short_code4 == '2':
                    print ("Enter Your Name")
                    user_name_run2= input()
                    print ("Your password has has been generated")
                    user_password_run2 = random.randint(10000,99000)

                    save_users(create_users(user_name_run2, user_password_run2))
                    print("\n")
                    print (f"New user created") 
                    print('-'*10)
                    print("user ...............password")
                    print(f" name:{user_name_run2}.... Password:{user_password_run2} ")

                    #This part invokes the credentials class
                    print ('-'*10)
                    print("You can now login to add a new credential")
                    print("enter \'ok'\' to continue")
                    print ('-'*10)
                
                elif short_code4 == 'ex' or 'ok':
                    break
                else:
                    print("Invalid input please use the short codes")


        elif short_code0 == 'ex':
            print ("Exiting Application")
            break

        elif short_code0 == 'du':
            if displaying_all_users():
                print("Here is a list of all users")
                print("\n")

                for user in displaying_all_users():
                    print(f"{user.name}....{user.password}")
                    print ("\n")
            else:
                print("\n")
                print("You have not created any users yet")
                print("\n")

        elif short_code0 == 'fu':
            print("enter the name of the used you want to search for")
            search_name =input()

            if check_if_user_exists(search_name):
                search_user = find_users(search_name)
                print ('-'*10)
                print(f"{search_user.name}....{search_user.password}")
                

            else:
                print('-'*10)
                print ("User under the given name does not exist")

        elif short_code0 == 'dl':
            print("enter the name of the used you want to Delete")
            delete_name =input()

            if check_if_user_exists(delete_name):
                delete_users(find_users(delete_name))
                print ('-'*10)
                print(f"user {delete_name} deleted")
                
            else:
                print('-'*10)
                print ("User under the given name does not exist")
                print("\n")


        else:
            print("Invalid input, please use the provided shortcodes")

if __name__ == '__main__':

    main()