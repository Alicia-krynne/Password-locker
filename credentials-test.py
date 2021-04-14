import unittest
from  credentials import Credentials

class TestCredentials(unittest.TestCase):


  def setUp(self): #all  test cases  follow the  rules  of the  class
    self.new_credentials = Credentials("Joonsbae","Wattpad","Pinpop2020!")


  def test_save_credentials(self):
    self.new_credentials.save_credentials()

    self.assertEqual(len(Credentials.credentials_list),1)











if __name__ == '__main__':
    unittest.main()
