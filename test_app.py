from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
from random import choice



            # game is already going
            #  with client.session_transaction() as change_session:
            #     change_session['is_game_on'] = True
            #     change_session['board'] = TEST_BOARD

            # no game running
            #  with client.session_transaction() as change_session:
            #     change_session['is_game_on'] = False
            #     res = client.get('/')


class BoggleSetUpTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # the rest of the code, obviously enough, written by Tor Kingdon
    

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2><button class="btn btn-outline-primary rounded btn-block" name="game_on" value="1">play game #1</button></h2>', html)
            

    def test_reset(self):
        with app.test_client() as client:
            res = client.get('/reset')
            self.assertEqual(res.status_code, 302)
            self.assertIs(session.get('is_game_on'), False)
            
            
class BoggleGameplayTests(TestCase):
    @classmethod
    def setUp(self):
        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess['board'] = [['K', 'U', 'J', 'M', 'I'], ['I', 'I', 'U', 'D', 'E'], ['C', 'V', 'K', 'S', 'O'], ['S', 'Z', 'E', 'R', 'S'], ['L', 'M', 'H', 'O', 'E']]
            sess['correct_words'] = ['mud', 'sod', 'zero', 'hoe']
            # new_correct_words = ['judo', 'mid', 'dose', 'hero', 'horse', 'mess']
            # not_in_dic_words = ['cvks', 'duks', 'ciiv', 'zerk']
            # not_on_board_words = ['sour', 'ducks', 'civic', 'reek']
            sess['game_num'] = '1'
            sess['highscore'] = '5'
    
    def test_board(self):
        res = self.client.get('/board?game_on=1')
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('<th colspan="5" class="boggle-board text-center">Game #1</th>', html)

    def test_played_word_correct(self):
        res = self.client.get('/played-word?word=judo')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['result'], 'ok')

    def test_played_word_not_on_board(self):
        res = self.client.get('/played-word?word=sour')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['result'], 'not-on-board')

    def test_played_not_word(self):
        res = self.client.get('/played-word?word=duks')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['result'], 'not-word')

    # def test_post_high_score(self):
    #     res = self.client.post('/post-score', data={"score": "9"})
    #     self.assertEqual(res.json['message'], 'new high score')

    # def test_post_tied_score(self):
    #     res = self.client.post('/post-score', data={"score": "5"})
    #     self.assertEqual(res.json['message'], 'you just tied the high score')

    # def test_post_score(self):
    #     res = self.client.post('/post-score', data={"score": "3"})
    #     self.assertEqual(res.json['message'], 'good game')

# class BoggleResultsTests(TestCase):
#     def test_display_results(self):
#         with app.test_client() as client:
#             res = self.client.get('/display-results?score=9')
#             html = res.get_data(as_text=True)
#             self.assertEqual(res.status_code, 200)
