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
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                board = [['K', 'U', 'J', 'M', 'I'], ['I', 'I', 'U', 'D', 'E'], ['C', 'V', 'K', 'S', 'O'], ['S', 'Z', 'E', 'R', 'S'], ['L', 'M', 'H', 'O', 'E']]
                correct_words = ['mud', 'sod', 'zero', 'hoe']
                new_correct_words = ['judo', 'mid', 'dose', 'hero', 'horse', 'mess']
                not_in_dic_words = ['cvks', 'duks', 'ciiv', 'zerk']
                not_on_board_words = ['sour', 'ducks', 'civic', 'reek']
                change_session['board'] = board
                change_session['correct_words'] = correct_words
                change_session['game_num'] = '1'
    
    def test_board(self):
        with app.test_client() as client:
            res = client.get('/board?game_on=1')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<th colspan="5" class="boggle-board text-center">Game #1</th>', html)

    def test_played_word_correct(self):
        with app.test_client() as client:
            res = client.get('/played-word?word=judo')
            self.assertEqual(res.status_code, 200)
