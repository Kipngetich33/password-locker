#!/usr/bin/env python3.6

from user import User

def create_user(name,password):
    '''
    Function that creates a new contact object by calling the class
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

def find_contacts(name):
    '''
    Functiont that searches for a user using the name of the user and returns the user
    '''
   return  User.find_user_by_name(name)

def check_if_user_exists(name):
