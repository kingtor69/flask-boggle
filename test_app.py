from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
from random import choice

TEST_BOARD = [['K', 'U', 'J', 'M', 'I'], ['I', 'I', 'U', 'D', 'E'], ['C', 'V', 'K', 'S', 'O'], ['S', 'Z', 'E', 'R', 'S'], ['L', 'M', 'H', 'O', 'E']]
TEST_SOME_CORRECT_WORDS = ['mud', 'sod', 'zero', 'hoe', 'judo', 'mid', 'dose', 'hero', 'horse', 'mess']
TEST_SOME_NOT_IN_DICT_WORDS = ['cvks', 'duks', 'ciiv', 'zerk']
TEST_SOME_NOT_ON_BOARD_WORDS = ['sour', 'ducks', 'civic', 'reek']


            # game is already going
            #  with client.session_transaction() as change_session:
            #     change_session['is_game_on'] = True
            #     change_session['board'] = TEST_BOARD

            # no game running
            #  with client.session_transaction() as change_session:
            #     change_session['is_game_on'] = False
            #     res = client.get('/')


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # the rest of the code, obviously enough, written by Tor Kingdon
    
    def test_home(self):
        with app.test_client() as client:
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
            self.assertIn('<td class="col text-center" id="0-0">', html)
            self.assertIn('<td class="col text-center" id="4-4">', html)

    def test_reset(self):
        with app.test_client() as client:
            res = client.get('/reset')
            self.assertEqual(res.status_code, 302)
            self.assertIs(session.get('is_game_on'), False)
            
    def test_correct_plays(self):
        correct = choice(TEST_SOME_CORRECT_WORDS)
        with app.test_client() as client:
            res = client.get(f'/play/?word={correct}')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn(f'<li>{correct}</li>')


    def test_non_word_plays(self):
        non_word = choice(TEST_SOME_NOT_IN_DICT_WORDS)
        with app.test_client() as client:
            res = client.get(f'/play/?word={non_word}')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<tag class="error pl-2 pr-2">Sorry, that word is not in our dictionary.</tag>', html)

    def test_non_board_plays(self):
        non_board = choice(TEST_SOME_NOT_ON_BOARD_WORDS)
        with app.test_client() as client:
            res = client.get(f'/play/?word={non_board}')
            html = res.get_data(as_test=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<tag class="error pl-2 pr-2">Sorry, that word is not on this board.</tag>', html)



