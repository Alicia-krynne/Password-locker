#!/usr/bin/env python3
from user import User
from credentials import Credentials


def create_user(first_name, last_name, email, password):
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
    new_credentials = Credentials(name, website, password)
    return new_credentials


def save_credentials(credentials):
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


while True:
	print("Hello Welcome to password-locker")
	print('\n')

	print(
					"select short code: new user - nu: , log in : -lg , exit password locker : -ex")
	short_code = input().lower()
	print('\n')

if short_code == 'nu':
	print("create username")
	created_user_name = input()

	print("create password")
	created_user_password = input()

	print("confirm password")
	confirm_user_pasword = input()

	while confirm_user_pasword != created_user_password:
		print("invalid!!! password did not match")
		print("enter created password")
		created_user_password = input()
		print("confirm password")
		confirm_user_pasword = input()

	else:
		print(
						"congratulations{created_user_name}! account  creation  succesfull")
		print('\n')
		print("proceed to  log in")
		print('\n')

elif short_code == 'lg':
	print("welcome!")
	print("Enter Username")
	created_user_name = input()

	print("Enter password")
	created_user_password = input()
	print('\n')

	while created_user_name != created_user_name or created_user_password != created_user_password:
		print("invalid entry")
		print("enter username")

		created_user_name = input()

		print("enter password")
		created_user_password = input()
		print('\n')
	else:
	print("log in  success")

  while True:
		print("what  do  you  want to do?:cn- create new credentials,sc- show credentials,fc- find credentials ")
		short_code = input().lower()

	if short_code == 'cn':  # created  and  saved the  credentials
			print("new_credentials")
			print("-"*10)

			print("name....")
			name = input()

			print("website ...")
			website = input()

			print("password ...")
			password = input()

			save_credentials(new_credentials(name, website, password)) 
			print('\n')
			print(f" new Credentials {name} {website} {password} created")
			print('\n')
			
	elif short_code == 'sc':
			if show_credentials(credentials):
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
					search_credential_by_website = find_credentials(search_credential_by_website)
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
