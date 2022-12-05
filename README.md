# 19.5.17 Flask Boggle

## Springboard Software Engineering Career Track
## Tor Kingdon

Boggle project using Flask and JavaScript, Python, Jinja, *&c.*

Plays like the dice game using code written by me **and** starter code provided by Colt Steele, Rithm School, and/or Springboard. (Starter code noted.)

The assignment used random letter chosen from an alphabet of all 26 characters, thus making it just as likely to get a ‘z’ as an ‘e.’ I created an “alphabet” (`./weighted_alphabet.py`) with duplicate letters to create an experience more like the game with more common letters more likely to appear than less common ones. 

There is a known bug which I am in the midst of debugging wherein the averages are calculated not including the most recent game played. This bug appeared on deployment, and does not show up on a development server, making debugging a bit tricky, but I’ll get it. :D
