#!/usr/bin/env python3
from user import User
from credentials import Credentials

def create_user(first_name,last_name,email,password):
    '''
    Function to create a new user
    '''
    new_user = User()
    return new_user


def save_user(user):
    User.user_list.append(self)


def delete_user(user):
    User.user_list.remove(self)


def find_user_by_email(email):
    return User.find_user_by_email
    

def new_credentials(credentials):
    new_credentials = Credentials()
    return new_credentials

def save_credentials (credentials):
    '''
    Function to save a credential
    '''
    Credentials.save_credentials()


def remove_credentials(credentials):
    '''
    Function to delete a credential
    '''
    Credentials.remove_credentials()

def credentials_available(website):
    return Credentials.search_credential_by_website

    """
    function  to  search  a credential
    """

def show_credentials(credentials):
    return Credentials.show_credentials
    

def main():
            print("Hello Welcome  What is your name?")
            new_user = input()

            print(f"Hello {new_user}. Choose action")
            print('\n')

            while True:
                    print( " cn- create new credentials,sc- show credentials,fc- find credentials, ex- exit",)

                    short_code = input().lower()
                    

                    if short_code == 'cn':  #created  and  saved the  credentials
                            print("new_credentials")
                            print("-"*10)

                            print ("name....")
                            name = input()

                            print("website ...")
                            website = input()

                            print("password ...")
                            password = input()

                            save_credentials(new_credentials(name,website,password)) 
                            print ('\n')
                            print(f" new Credentials {name} {website} {password} created")
                            print ('\n')
                    elif short_code == 'sc':
                            if show_credentials():
                                    print("Here  you  go ^_^")
                                    print('\n')

                                    for credentials in show_credentials():
                                            print(f"{credentials.name} {credentials.website} .....{credentials.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("no  credentials, try  adding")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the credentials you want to search for")

                            credentials_available = input()
                            if search_credential_by_website(search_credential_by_website):
                                    search_credential_by_website= find_credentials(search_credential_by_website)
                                    print(f"{find_credential.name} {find_credential.website} {find_credential.password}")
                                    print('-' * 20)

                                    print(f"name .......{find_credential.name}")
                                    print(f"website.......{find_credential.website}")
                                    print(f"password.......{find_credential.password}")
                                   
                            else:
                                    print("That  entry does not exist")
                    elif short_code == 'ex':
                            print("Bye  have  a  swell  day .......")
                            break
                   
                    else:
                            print("I really didn't get that. Please use the short codes")

                            

                    
if __name__ == '__main__':
    main()


