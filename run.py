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
        print ('-'*10)
        print("PLEASE USE THE FOLLOWING SHORT CODES:")
        print ('-'*10)
        print("lg : to LOGIN") 
        print("cu : to CREATE NEW USER")
        print("fu : to FIND A USER")
        print("du : to DISPLAY ALL USERS")
        print("ex : to EXIT")
        short_code0= input()
        if short_code0 == 'lg':
                print("ENTER USER NAME")
                login_user_name= input()
                print("ENTER PASSWORD")
                login_password = input()

                if check_if_user_exists(login_user_name):
                    print(f"WELCOME {login_user_name}") 
                    logged_in_user = find_users(login_user_name)

                    if logged_in_user.password == login_password:

                        print(f"{logged_in_user.name} ...........{logged_in_user.password}")
                        print ('-'*10)

                        while True:
                            print ('-'*10)
                            print("PLEASE USE THE FOLLOWING SHORTCODES")
                            print ('-'*10)
                            print("cc :to ADD A CREDENTIAL")
                            print("dc :to DISPLAY CREDENTIALS") 
                            print("dl :to DELETE A CREDENTIAL")
                            print("ex :to EXIT")
                            shortcode3 = input()

                            credential_user_name = logged_in_user.name

                            if shortcode3 == 'cc':

                                while True:
                                    print ('-'*10)
                                    print("USE THE FOLLOWING SHORTCODES")
                                    print ('-'*10)
                                    print("1 :to ENTER YOUR OWN PASSWORD")
                                    print("2 : to GET SYSTEM GENERATED PASSWORD")
                                    print("ok : to GO BACK TO THE CREDENTIALS MENU")
                                    short_code5 = input()

                                    if short_code5 == '1':
                                        print(f"WELCOME {credential_user_name}, ADD A CREDENTIAL") 
                                        print ('-'*10)
                                        print("ENTER CREDENTIAL NAME")
                                        name_of_credential =input()
                                        print("ENTER CREDENTIAL'S PASSWORD")
                                        password_of_credential = input()

                                        save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                        
                                        print("YOUR CREDENTIALS")
                                        print ('-'*10)
                                        for credential in Credentials.display_all_credentials():
                                            if credential_user_name == credential.user_name:
                                                print(f"CREDENTIAL:{credential.credential_name}......PASSWORD:{credential.credential_password}")
                                                print ("\n")
                                    

                                    elif short_code5 == '2':
                                        print ('-'*10)
                                        print(f"WELCOME {credential_user_name}, ADD A CREDENTIAL")
                                        print ('-'*10) 
                                        print("ENTER CREDENTIAL NAME")
                                        name_of_credential =input()
                                        print("YOUR PASSWORD HAS BEEN GENERATED")
                                        password_of_credential = random.randint(10000,99000)

                                        save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                        
                                        print("YOUR CREDENTIALS")
                                        print ('-'*10)
                                        for credential in Credentials.display_all_credentials():
                                            if credential_user_name == credential.user_name:
                                                print(f"CREDENTIAL:{credential.credential_name}......PASSWORD:{credential.credential_password}")
                                                print ("\n")

                                    elif short_code5 == 'ok':
                                        break

                                    elif short_code5 == 'ex':
                                        break
                                    else:
                                         print("INVALID INPUT PLEASE USE THE PROVIDED SHORTCODES")
                                         print ("\n")


                            elif shortcode3 == 'dc':
                                print("YOUR CREDENTIALS")
                                print ('-'*10)
                                for credential in Credentials.display_all_credentials():
                                    if credential_user_name == credential.user_name:
                                        print(f"{credential.credential_name}......{credential.credential_password}")
                                        print ("\n")

                            elif shortcode3 == 'dl':
                                if Credentials.credential_exists(credential_user_name):
                                    print("ENTER NAME OF CREDETIAL TO DELETE")
                                    credential_for_delete = input()

                                    for credential in Credentials.display_all_credentials():
                                        if credential.credential_name == credential_for_delete:
                                            credential.delete_credentials()
                                            print(f"DELETED {credential_for_delete}")
                                            print("\n")

                                        else:
                                            print ('-'*10)
                                            print("THE ENTERED CREDENTIAL DOES NOT EXIST")
                                            print ("\n")
        
                                else:
                                    print("YOU HAVE NOT ADDED ANY CREDENTIALS YET")   
                                    print ("\n")     

                            elif shortcode3 == 'ex':
                                print("EXITING CREDENTIALS")
                                print ("\n")
                                break

                            else:
                                print("INVALID CHOICE PLEASE USE THE PROVIDED SHORTCODES")
                                print ("\n")
                            
                else:
                   print ('-'*10)
                   print("WRONG USER/PASSWORD COMBINATION")
                   print ('-'*10)


<<<<<<< HEAD
        elif short_code0 == 'cu':
            print ("CREATING A NEW USER")
            print('-'*10)

            print ("ENTER YOUR NAME")
            user_name_run2 = input()
            print ("ENTER A PASSWORD")
            user_password_run2 =input()

            save_users(create_users(user_name_run2, user_password_run2))
            print("\n")
            print (f"NEW USER CREATED") 
            print('-'*10)
            print("USER ...............PASSWORD")
            print(f" NAME:{user_name_run2}.... PASSWORD:{user_password_run2} ")
            print ("\n")

            #This part invokes the credentials class
            print ('-'*10)
            print("YOU CAN NOW LOGIN TO ENTER A CREDENTIAL")
            print ('-'*10)

        elif short_code0 == 'ex':
            print ("EXITING APPLICATION")
            print ("\n")
            break

        elif short_code0 == 'du':
            if displaying_all_users():
                print("HERE IS A LIST OF ALL THE USERS")
                print("\n")

                for user in displaying_all_users():
                    print(f"{user.name}....{user.password}")
                    print ("\n")
            else:
                print("\n")
                print("YOU HAVE NOT CREATED ANY USERS YET")
                print("\n")

        elif short_code0 == 'fu':
            print("ENTER NAME OF THE USER YOU WANT TO SEARCH FOR")
            search_name =input()

            if check_if_user_exists(search_name):
                search_user = find_users(search_name)
                print ('-'*10)
                print(f"{search_user.name}....{search_user.password}")
                print ("\n")
                

            else:
                print('-'*10)
                print ("USER UNDER THE GIVEN NAME DOES NOT EXIST")
                print ("\n")
                

        elif short_code0 == 'dl':
            print("ENTER NAME OF USER YOU WANT TO DELETE")
            delete_name =input()

            if check_if_user_exists(delete_name):
                delete_users(find_users(delete_name))
                print ('-'*10)
                print(f"USER {delete_name} DELETED")
                print ("\n")
                
            else:
                print('-'*10)
                print ("USER UNDER THE GIVEN NAME DOES NOT EXIST")
                print("\n")


        else:
            print("INVALID CHOICE PLEASE USE THE PROVIDED SHORTCODES")

if __name__ == '__main__':

    main()