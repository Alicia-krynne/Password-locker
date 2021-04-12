class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty  list

    def __init__(self,user_name,account_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.account_name = account_name
        self.password =password

def save_user(self):

        '''
       saves users  objects into user_list
        '''

        User.user_list.append(self)


def delete_user(self):

        '''
        delete_user method deletes a saved users  from the user_list
        '''

       User.user_list.remove(self)
@classmethod
def display_user(cls):
        '''
        method that returns the users  list
        '''
        return cls.user_list
