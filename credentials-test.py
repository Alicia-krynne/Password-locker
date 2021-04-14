import unittest
from  credentials import Credentials


class TestCredentials(unittest.TestCase):


  def setUp(self): #all  test cases  follow the  rules  of the  class
    self.new_credentials = Credentials("Joonsbae","Wattpad","Pinpop2020!")


  def test_save_credentials(self):
    self.new_credentials.save_credentials()

    self.assertEqual(len(Credentials.credentials_list),1)


  def tearDown(self): # redefine  the  class  to  accept  more    users.
    Credentials.credentials_list = []


  def test_add_more_credentials(self):
    self.new_credentials.save_credentials()
    newCredential = Credentials("namjoon","weverse","bangtan613")
    newCredential.save_credentials()
     
    self.assertEqual(len(Credentials.credentials_list),2)

  def test_remove_credentials(self):
    self.new_credentials.save_credentials()
    newCredential = Credentials("namjoon","weverse","bangtan613")
    newCredential.save_credentials()

    newCredential.remove_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_search_credential_by_website(self):
    self.new_credentials.save_credentials()
    newCredential = Credentials("namjoon","weverse","bangtan613")
    newCredential.save_credentials()

    find_credential = Credentials.search_credential_by_website("weverse")
    self.assertEqual(find_credential.website,newCredential.website)

  def test_credentials_available(self):
    self.new_credentials.save_credentials()
    newCredential = Credentials("namjoon","weverse","bangtan613")
    newCredential.save_credentials()

    credentials_available = Credentials.credentials_available("weverse")
    self.assertTrue(credentials_available)


  def test_show_credentials(self):
    self.assertEqual(Credentials.show_credentials(),Credentials.credentials_list)

  




if __name__ == '__main__':
    unittest.main()
