from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from random import choice
from boggle import Boggle, this_game, compliments, nicknames

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"

@app.route('/')
def load_home_page():
    """load home page to display high score, number of games played, average score"""

    highscore = int(session.get('high_score', '0'))
    average_score = int(session.get('average_score', '0'))
    game_num = int(session.get('game_num', '0'))
    # if the game_num says games have been played and either of the other numbers are zero, something is wonky, so just reset and start over
    if highscore == 0 or averagescore == 0:
        session.clear()
    session['highscore'] = highscore
    session['average_score'] = average_score
    session['game_num'] = game_num
    return render_template('home.html', highscore = highscore, game_num = game_num, average_score = average_score)

@app.route('/board')
def load_board():
    """set up the board and the game-play form"""
    # raise
    # request.args is giving me a lot of attitude right now, so I'm commenting it out whole I get the JS going
    # if not request.args['game_on']:
    #     flash('something went wrong, please try again', 'info')
    #     return redirect('/')

    # the game number returns from the form is incremented 1 from where it had been previously, so these lines are incrementing the game number
    # game_num = request.args['game_on']
    # session['game_num'] = game_num
    correct_words = session.get('correct_words', [])
    this_game = Boggle()
    board = this_game.make_board()
    session['board'] = board
    flash("Let's play!", "info")
    return render_template('game.html', board = board, len_correct_words = len(correct_words))

@app.route('/played-word')

# @app.route('/play')
# def play_a_word():
#     word = request.args['word']
#     board = session['board']
#     correct_words = session.get('correct_words', [])
#     is_word_valid = this_game.check_valid_word(board, word)
#     if is_word_valid == "ok":
#         if correct_words.count(word) > 0:
#             flash (f"You already got that word, {choice(nicknames)}.", "info")
#         else:
#             correct_words.append(word)
#             session['correct_words'] = correct_words
#             flash (choice(compliments), "thanks")
#     else:
#         flash (f"Sorry, {choice(nicknames)}, that word is {is_word_valid}.", "error")    
#     return render_template('board.html', board = board, len_correct_words = len(correct_words))

@app.route('/reset')
def reset_session_restart():
    session.clear()
    session['is_game_on'] = False
    return redirect ('/')