class Credentials :


  credentials_list= [] 

  def __init__(self,name,website,password):
        self.name = name
        self.website = website
        self.password = password


  def save_credentials(self):
          Credentials.credentials_list.append(self)

  def add_more_credentials(self):
          Credentials.credentials_list.append(self)


  def remove_credentials(self):
          Credentials.credentials_list.remove(self)


  @classmethod  # after  calling the  class method, always  asign the  key  word cls to the  funtion
  def search_credential_by_website(cls,website):
        for credential in cls.credentials_list:
            if credential.website == website:
                return credential # this  loop  goes thru  all  user info to  find  the  email and  return  their   full details
    

  @classmethod # to  allow input
  def credentials_available(cls,website):
        for credential in cls.credentials_list:
            if credential.website == website:
                return True
        return False

 