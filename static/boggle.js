// Can you guess who wrote the JavaScript? That's right, Tor Kingdon, the same guy who wrote this console.log:
// console.log("What is this javascript stuff all about? And jQuery‽ I forgot. Let's see........")
// I also borrowed liberally from the solution code by Rithm School and/or Springboard

compliments = ["Good one", "Nice", "Niiiiice", "Beauty, eh?", "Slick", "You're killing it", "Daddy needs a new pair of shoes", "Snappy", "Momma's gotta bring home the bacon", "Yo", "Muey caliente", "Delicious", "Gans genau", "Trés bien"]
nicknames = ["slick", "fancypants", "homeslice", "cheeseball", "dog", "tiny", "biggie", "sneaky pie", "homey", "amigo", "knucklehead", "big dog", "two times", "shorty", "punch buggy", "buckethead", "grandma pumpkinhead", "homes", "bobby-bob"]

function getRandomItem(arr) {
    const randomI = Math.floor(Math.random() * arr.length);
    return arr[randomI]
};
let messageCount = 0;

class GameOBoggle {
    constructor(gameId, gameLength = 60, boardSize = 5) {
        // game_length measured in seconds
        this.secondsLeft = gameLength;
        this.boardSize = boardSize;
        this.showTimeLeft();

        this.gameScore = 0;
        this.doneWords = new Set();
        this.game = $("#" + gameId)

        // of course JS works in msec, so each second is sent out every 1000 ms
        this.countdownClock = setInterval(this.second.bind(this), 1000);

        // define new word submit button. yeah, it's kinda important for playing the game, ya know?
        document.addEventListener("DOMContentLoaded", (domLoadedEvt) => {
            $(".word-submit-form", this.game).on("submit", this.processNewWord.bind(this))
        });
    }

    // add new row to scoring table with new word and word score
    displayScore(word, wordScore) {
        const wordTd = document.createElement('td');
        const scoreTd = document.createElement('td');
        wordTd.innerText = word;
        scoreTd.innerText = wordScore;
        const scoringTr = document.createElement('tr');
        scoringTr.appendChild(wordTd);
        scoringTr.appendChild(scoreTd);
        const scoringTbody = document.querySelector('.scoring')
        scoringTbody.appendChild(scoringTr)
    }

    // jQuery was driving me bananas
    displayScoreJQ(word, wordScore) {
        debugger;
        const $wordTd = $('td.word');
        const $scoreTd = $('td.score');
        $wordTd.text = word;
        $scoreTd.text = wordScore;
        const $scoringTr = $('tr');
        $scoringTr.append($wordTd);
        $scoringTr.append($scoreTd);
        console.log($scoringTr)
        $('tbody.scoring', this.game).append($scoringTr);
    }

    // scoring algorithm adapted by Tor rather loosely from official Boggle scoring for various table sizes as found on https://en.wikipedia.org/wiki/Boggle
    scoreWord(word) {
        let score = 0;
        // 5x5 minimum 3-letter words
        // 6x6 minimum 4-letter words
        if (word.length > Math.floor(this.boardSize/2)) {
            score ++
        }
        // 5x5 2 points for 4-letter words
        // 6x6 2 points for 5-letter words
        if (word.length >= this.boardSize*0.8) {
            score ++
        }
        // 5x5 3 points for 5-letter words
        // 6x6 3 points for 6-letter words
        if (word.length >= this.boardSize) {
            score ++
        }
        // 5x5 5 points for 6-letter words
        // 6x6 5 points for 8-letter words
        if (word.length >= this.boardSize*1.2) {
            score += 2
        }
        // 5x5 8 points for 7-letter words
        // 6x6 8 points for 9-letter words
        if (word.length >= this.boardSize*1.4) {
            score += 3
        }
        // 5x5 8th and subsequent letters worth 2 points each
        // 6x6 10th letter worth 4 points, 2 points for each letter after that
        if (score >= 8) {
            score += ((word.length - (Math.floor(this.boardSize*1.4))) *2)
        }
        return score
    }

    displayMessage(message, type, stayForMsecs = 1500) {
        const $messages = $("#messages", this.game);
        $messages
            .text('')
            .removeClass();
        $messages
            .text(message)
            .removeClass()
            .addClass(`tags ${type}`);
        messageCount ++
        setTimeout(()=> {
            $messages
                .text('')
                .removeClass();
        }, stayForMsecs);
    }

    async processNewWord(evt) {
        evt.preventDefault();
        const $newWord = $('#new-word', this.game)
        const newWord = $newWord.val()
        $newWord.val('').focus();
        if (!newWord) return;
        if (this.doneWords.has(newWord)) {
            this.displayMessage(`You already got ${newWord}, ${getRandomItem(nicknames)}`, "error")
            return;
        }
        const respnse = await axios.get("/played-word", { params: { word: newWord }});
        if (respnse.data.result === "not-word") {
            this.displayMessage(`"${newWord}" is not in our dictionary, ${getRandomItem(nicknames)}`, "error")
        } else if (respnse.data.result === "not-on-board") {
            this.displayMessage(`"${newWord}" is not a valid play on this board, ${getRandomItem(nicknames)}`, "error")
        } else {
            let wordScore = this.scoreWord(newWord);
            if (wordScore == 0) {
                this.displayMessage(`"${newWord}" is not long enough, ${getRandomItem(nicknames)}`, "error");
            } else {
                this.displayScore(newWord, wordScore)
                this.gameScore += wordScore;
                $('.running-score').text(this.gameScore)
                this.doneWords.add(newWord);
                this.displayMessage(`${getRandomItem(compliments)}, ${getRandomItem(nicknames)}`, "info");
            }
        }
    }

    // display timer in DOM
    showTimeLeft() {
        $(".timer", this.game).text(this.secondsLeft)
    }

    // run the timer

    async second() {
        this.secondsLeft -= 1;
        this.showTimeLeft()

        if (this.secondsLeft === 0) {
            clearInterval(this.countdownClock);
            await this.endGame();
        }
    }

    async endGame() {
        $('.word-submit-form', this.game).hide();
        const resp = await axios.post("/post-score", { score: this.gameScore });
        console.log(resp)
        this.displayMessage(`${getRandomItem(compliments)}! ${resp.data.message} ${getRandomItem(nicknames)}.`, resp.data.class, 3000)
        setTimeout(window.location.replace("/"), 5000);
    }
}
