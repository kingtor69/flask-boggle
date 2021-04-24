from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

TEST_BOARD = [['A','B','C','D','E'], ['F','G','H','I','J'], ['K','L','M','N','O'], ['P','Q','R','S','T'], ['U','V','W','X','Y']]

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # the rest of the code, obviously enough, written by Tor Kingdon
    def test_home_game_on(self):
        with app.test_client() as client:
             with client.session_transaction() as change_session:
                change_session['is_game_on'] = True
                change_session['board'] = TEST_BOARD
                res = client.get('/')
                html = res.get_data(as_text=True)
                self.assertEqual(res.status_code, 200)
                self.assertIn('Game #', html)
                self.assertEqual(len(board), 5)
                self.assertEqual(len(board[3]), 5)
    
    def test_home_game_off(self):
        with app.test_client() as client:
             with client.session_transaction() as change_session:
                change_session['is_game_on'] = False
                res = client.get('/')
                html = res.get_data(as_text=True)
                self.assertEqual(res.status_code, 200)
                self.assertIn('<h2><button class="btn btn-outline-primary rounded btn-block" name="play" value="True">', html)
                self.assertIn("Let's Play!</button></h2>", html)
            
    def test_board(self):
        with app.test_client() as client:
            res = client.get('/board')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('Game #', html)
            self.assertEqual(len(board), 5)
            # self.assertEqual(len(board[3]), 5)

    def test_reset(self):
        with app.test_client() as client:
            res = client.get('/reset')
            self.assertEqual(res.status_code, 200)
            self.assertIs(session.get('is_game_on'), False)
            