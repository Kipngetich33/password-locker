#!/usr/bin/env python3.6

from user import User
from credetials import Credentials

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

def main():
    print("Welcome to Password Locker. What is you name?")
    user_name_run =input()
    print("\n")
    print(f"What would you like to do {user_name_run}")
    while True:
        print ("Use these short code: cu -create user ,du -displays users ,fu -find a user ,ex -exit")
        short_code =input()

        if short_code == 'cu':
            print ("New User")
            print('-'*10)

            print ("Enter Your Name")
            user_name_run2= input()
            print ("Enter a password")
            user_password_run2 =input()

            save_users(create_users(user_name_run2, user_password_run2))
            print("\n")
            print (f"New user created {user_name_run2} {user_password_run2} ")

        elif short_code == 'du':
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

        elif short_code == 'fu':
            print("enter the name of the used you want to search for")
            search_name =input()

            if check_if_user_exists(search_name):
                search_user = find_users(search_name)
                print(f"{search_user.name}")
                print ('-'*10)
                print (f"{search_user.password}")

            else:
                print ("User under the given name does not exist")

        elif short_code == 'ex':
            print ('Existing Application')
            break
        else:
            print("Invalid input please try again using the given shortcodes")

if __name__ == '__main__':

    main()