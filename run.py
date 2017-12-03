#!/usr/bin/env python3.6

from user import User
from credetials import Credentials

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
        print("please use the shortcodes lg-login, ca- create a new account ex- exit")
        short_code0= input()
        if short_code0 == 'lg':
                print("Enter User Name")
                login_user_name= input()
                print("Enter Password")
                login_password = input()

                if check_if_user_exists(login_user_name):
                    print("loop")
                    logged_in_user = find_users(login_user_name)

                    if logged_in_user.password == login_password:

                        print(f"{logged_in_user.name} .....{logged_in_user.password}")
                        print ('-'*10)
                        while True:
                            print("Enter ca- to add another credential , ex -exit")
                            shortcode3 = input()

                            if shortcode3 == 'ca':
                                credential_user_name = logged_in_user.name
                                print(f"welcome {credential_user_name} add a credential") 
                                print("Enter credential name")
                                name_of_credential =input()
                                print("Enter password for the credential")
                                password_of_credential = input()

                                save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                print("passed this ")
                                print(f"credentials Credentials.find_credentials_by_name(credential_user_name)")
                                print("\n")
                                # for credential in :
                                    # if 
                                    # print(credential_name, credential_password)

                            elif shortcode3 == 'ex':
                                print("exiting credentials")
                                break                            
                            
                            print ('-'*10)
                            print("\n")


                        print("Enter name")
                else:
                    print("\n")
                    print("Wrong user name and password combination")


        elif short_code0 == 'ca':
            print ("New User")
            print('-'*10)

            print ("Enter Your Name")
            user_name_run2= input()
            print ("Enter a password")
            user_password_run2 =input()

            save_users(create_users(user_name_run2, user_password_run2))
            print("\n")
            print (f"New user created {user_name_run2} {user_password_run2} ")

            #This part invokes the credentials class
            print("\n")
            print("You can now login to add a new credential")
             


        elif short_code0 == 'ex':
            print ("Exiting Application")
            break
        else:
            print("Invalid input, please use the provided shortcodes")

    # print("Welcome to Password Locker. What is you name?")
    # user_name_run =input()
    # print("\n")
    # print(f"What would you like to do {user_name_run}")
    # while True:
    #     print ("Use these short code: cu -create user ,du -displays users ,fu -find a user ,ex -exit")
    #     short_code =input()

    #     if short_code == 'cu':
    #         print ("New User")
    #         print('-'*10)

    #         print ("Enter Your Name")
    #         user_name_run2= input()
    #         print ("Enter a password")
    #         user_password_run2 =input()

    #         save_users(create_users(user_name_run2, user_password_run2))
    #         print("\n")
    #         print (f"New user created {user_name_run2} {user_password_run2} ")

    #         # This part invokes the credentials class
    #         print("\n")
    #         print("You can now add a new credential")

    #         while True:
    #             print("ss-create and save , dc-display credentials, ex -exit")
    #             short_code2 =input()

    #             if short_code2 == 'ss':
    #                 print("Enter username")
    #                 credential_user_name = input()
    #                 print("Enter name of credential")
    #                 credential_name = input ()
    #                 print("Enter password of credential")
    #                 credential_password = input()

    #                 save_credential_run(create_credential(credential_user_name, credential_name,credential_password))
    #                 print("A new creditial has been created")
    #             # elif short_code2 == 'dl':
    #             #     print("ok")
    #             #     break

    #             # elif short_code2 == 'dc':




    #     elif short_code == 'du':
    #         if displaying_all_users():
    #             print("Here is a list of all users")
    #             print("\n")

    #             for user in displaying_all_users():
    #                 print(f"{user.name}....{user.password}")
    #                 print ("\n")
    #         else:
    #             print("\n")
    #             print("You have not created any users yet")
    #             print("\n")

    #     elif short_code == 'fu':
    #         print("enter the name of the used you want to search for")
    #         search_name =input()

    #         if check_if_user_exists(search_name):
    #             search_user = find_users(search_name)
    #             print(f"{search_user.name}")
    #             print ('-'*10)
    #             print (f"{search_user.password}")

    #         else:
    #             print ("User under the given name does not exist")

    #     elif short_code == 'ex':
    #         print ('Existing Application')
    #         break
    #     else:
    #         print("Invalid input please try again using the given shortcodes")

if __name__ == '__main__':

    main()