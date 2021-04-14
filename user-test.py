import unittest 
from  user import User

class TestUser(unittest.TestCase):

  def setUp(self): #all  test cases  follow the  rules  of the  class
    self.new_user = User("Alice","clown","clown@clown.com","Pinpop2020!")


  def test_save_user(self):
    self.new_user.save_user()

    self.assertEqual(len(User.user_list),1)

  def tearDown(self): # redefine  the  class  to  accept  more    users.
    User.user_list = []

  def test_save_multiple_users(self):
     self.new_user.save_user()
     user2 = User("kimani","mbugua","kimani@gmail.com","kimani13%")
     user2.save_user()
     
     self.assertEqual(len(User.user_list),2)
  
  def test_delete_user(self):  # always  remeber the  self and :
    self.new_user.save_user()
    user2 = User("kimani","mbugua","kimani@gmail.com","kimani13%")
    user2.save_user()

    user2.delete_user()
    self.assertEqual(len(User.user_list),1)





if __name__ == '__main__':
    unittest.main()
