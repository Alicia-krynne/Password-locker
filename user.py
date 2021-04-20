class User :
#this is  a doc string below  here 

    """
     Class that generates new instances of User
    """

    user_list = [] 

    def __init__ (self,username ,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name:     user name  for  new  user
           password : password to  app  locker 
            

        '''
        self.user_name = user_name
        self.password = password


    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    '''
        @classmethod  # after  calling the  class method, always  asign the  key  word cls to the  funtion
        def find_user_by_email(cls,email):
            for user in cls.user_list:
                if user.email == email:
                    return user # this  loop  goes thru  all  user info to  find  the  email and  return  their   full details
        

        @classmethod # to  allow input
        def user_exists(cls,email):
            for user in cls.user_list:
                if user.email == email:
                    return True
            return False

        @classmethod
        def display_users(cls): #since nothing  was passed in the  test  we just need the  cls
            return cls.user_list
    '''

