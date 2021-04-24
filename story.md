# Flask Boggle
## The Story
    1. load home page with "let's play button to start"
        - check session if there's a game in progress
        - I've also got the session clear button that I put in the surveys
    2. new board loads 
        - create new dict from class Boggle
        - random 26-letter assignment for each of 25 spaces in 5x5 list of lists is created in Boggle.make_board
        - it'll have a own path and html template

## Session keys:
    - is_game_on: boolean
    - board: list of lists for letter assignments in 5x5 board