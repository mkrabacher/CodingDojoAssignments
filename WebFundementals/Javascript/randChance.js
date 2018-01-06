function gamble(walkAway = 200) {
    var quarters = 10,
        winnings = 0;

    function rollDemDice() {
        var win = 0;
        quarters -= 1;
        chance = (Math.floor(Math.random() * 25));
        console.log('lucky number: ' + chance);
        if(chance == 5) {
            win = (Math.floor(Math.random() * 51) + 50);
            quarters += win;
            winnings += win;
            return 'win';
        } else {
            return 'FAIL!';
        }  
    }

    while (quarters > 0) {
        if(quarters > walkAway) {
            return console.log("that's my number. I'm outta here.");
        }
        console.log(rollDemDice())
        console.log("q's:" + quarters)
    }
    console.log("You won a total of " + winnings + " quarters. and walked away with " + quarters + " quarters.")
}

gamble(100)