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
          