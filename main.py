#!/usr/bin/env python3
from password import User
from credentials import Credentials

def create_user(fname,lname,phone):
    '''
    Function to create a new user
    '''
    new_user = user(fname,lname)
    return new_contact
def save_credentials (credential):
    '''
    Function to save a credential
    '''
    credential.save_credentials()
def del_crdentials(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credentials()

def main():
            print("Hello Welcome  What is your name?")
            user_name = input()

            print(f"Hello {user_name}. Choose action")
            print('\n')

            while True:
                    print("Action: cd - create a new credentials, dc - delete credentials,sc -  save credential ")

                    short_code = input().lower()

                    if short_code == 'cd':
                            print("New Credentials")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                          
                            save_credentials(create_user(f_name,l_name,p_number)) 
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')
                    elif short_code == "dc":
                            print("Bye .......")
                            break

                    else:
                            print("delete  credentials")
if __name__ == '__main__':

    main()


