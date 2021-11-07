from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Ray254 = User(username = 'Ray254',password = '1234', email = 'raytwit660@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Pickup',pitch_comment='yoh men whats good',category="interview",user = self.user_Ray254,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_Ray254,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Ray254)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)