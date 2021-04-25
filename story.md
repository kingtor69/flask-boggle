# Flask Boggle
## The Story
    1. load home page with "let's play button to start"
        - check session if there's a game in progress
        - I've also got the session clear button that I put in the surveys
    2. new board loads 
        - create new dict from class Boggle
        - random 26-letter assignment for each of 25 spaces in 5x5 list of lists is created in Boggle.make_board
        - it'll have a own path and html template
    3. player enters a word
        - Boggle class has logic to test for a word being a word on the word-list and on the board
        - return message (not a word, or not on board) for incorrect guesses
        - display compliment and add word to list on the page if it's a good one


## Session keys:
    - is_game_on: boolean
    - board: list of lists for letter assignments in 5x5 board
    - correct_words: list of words that have been confirmed
    - game_num: keep a count of how many games user has played

## STILL DO TO:
    - my word list tests are not working, might have to skip the idea of being random?
    - fix tile sizes to be uniform
    - double-check the assignment
    - pretty sure session['is_game_on'] is pointless, since it's showing False as I play

## time permitting:
    - style up the word form