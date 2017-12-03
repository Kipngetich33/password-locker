#!/usr/bin/env python3.6

from user import User

def create_user(name,password):
    '''
    Function that creates a new contact object by calling the class
    '''
    new_run_user= User(name,password)
    return new_run_user

def save_users(contact):
    '''
    Function that saves the created user to the list of users
    '''
    contact.save_user()

# def delete_users(contact):
#     '''
#     Function that deletes a user
#     '''
#     contact.delete_user()

