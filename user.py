class User :
#this is  a doc string below  here 

    """
     Class that generates new instances of User
    """

    user_list = [] 

    def __init__ (self,first_name,last_name,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New user first name.
            last_name : New user last name.

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)
