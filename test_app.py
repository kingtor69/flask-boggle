from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


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