$(document).ready(function() {
    var map1 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],                // 0 = blank
        [1,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1],                // 1 = wall
        [1,2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,2,1],                // 2 = coin
        [1,2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,2,1],                // 3 = cherry
        [1,2,2,2,2,2,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,1],                // 4 = Start_p1_loc
        [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],                // 5 = loopA
        [1,2,2,2,2,2,2,1,1,2,2,2,2,1,2,2,2,2,1,1,2,2,2,2,2,2,1],                // 6 = loopB
        [1,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,1],                // 7 = start_p2_loc
        [1,1,1,1,1,1,2,1,1,1,1,1,0,1,0,1,1,1,1,1,2,1,1,1,1,1,1],                // 8 = ghost_start
        [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,1,8,0,0,0,8,1,0,1,1,2,1,1,1,1,1,1],                //
        [5,0,0,0,0,0,2,2,0,0,1,0,0,0,0,0,1,0,0,2,2,0,0,0,0,0,6],                //
        [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,1,8,0,0,0,8,1,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
        [1,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,1],
        [1,3,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1],
        [1,2,2,2,1,1,2,2,3,2,2,2,2,4,2,2,2,2,2,2,2,1,1,2,2,2,1],
        [1,1,1,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1],
        [1,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,2,1],
        [1,2,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
        [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

    var map2 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],                // 0 = blank
        [1,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1],                // 1 = wall
        [1,2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,2,1],                // 2 = coin
        [1,2,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,2,1],                // 3 = cherry
        [1,2,2,2,2,2,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,1],                // 4 = Start_p1_loc
        [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],                // 5 = loopA
        [1,2,2,2,2,2,2,1,1,2,2,2,2,1,2,2,2,2,1,1,2,2,2,2,2,2,1],                // 6 = loopB
        [1,1,1,1,1,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,1],                // 7 = start_p2_loc
        [1,1,1,1,1,1,2,1,1,1,1,1,0,1,0,1,1,1,1,1,2,1,1,1,1,1,1],                // 8 = ghost_start
        [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,0,8,0,0,0,8,0,0,0,0,0,0,0,1,1,1,1],                //
        [5,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],                //
        [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,0,8,0,0,0,8,0,0,0,0,0,0,0,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],                //
        [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
        [1,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,1],
        [1,3,1,1,1,1,2,1,1,1,1,2,1,1,1,2,1,1,1,1,2,1,1,1,1,2,1],
        [1,2,2,2,1,1,2,2,3,2,2,2,2,4,2,2,2,2,2,2,2,1,1,2,2,2,1],
        [1,1,1,2,1,1,2,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,2,1,1,1],
        [1,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,2,1],
        [1,2,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
        [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    
    var charDispPos = {},           //player 1
        charMapPos = {},
        charDirection = '',
        char2DispPos = {},          //player 2
        char2MapPos = {},
        char2Direction = '',
        map = map1,                 //map variables
        loopA = {},
        loopB = {},
        nomSong = new Audio('nomSong.wav');
        ghostsDispPos = []          //ghost things
        ghostsMapPos = []
        ghostsInPlay = 0;
        ghostsMoves = 0;

    function drawMap(arr) {
        var output = '';
        for(i = 0; i < arr.length; i++) {
            output += '<div class="row">'
            for(j = 0; j < arr[i].length; j++) {
                if(arr[i][j] == 1) {
                    output += '<div class="wall"></div>'
                } else if(arr[i][j] == 2) {
                    output += '<img class="coin" src="coin.gif"></img>'
                } else if(arr[i][j] == 3) {
                    output += '<img class="power-up" src="power-up.png"></img>'
                } else if(arr[i][j] == 5) {
                    loopA = {y:i,x:j};
                    output += '<div class="blank"></div>';
                } else if(arr[i][j] == 6) {
                    loopB = {y:i,x:j};
                    output += '<div class="blank"></div>';
                } else {
                    output += '<div class="blank"></div>';
                }
            }   
            output += '<div id="ghosts"></div></div>'
        }
        $('#frame').html(output);
    };

    function drawPacman(arr, p2 = false) {
        for(i = 0; i < arr.length; i++) {
            for(j = 0; j < arr[i].length; j++) {
                if(arr[i][j] == 4) {
                    charMapPos = {y:i,x:j, name:'pacman', moveCT:0, score:0};
                    charDispPos = {y:(i * 32),x:(j * 32 )};
                    $("#pacman").css('top', (charDispPos.y + 'px'))
                    $("#pacman").css('left', (charDispPos.x + 'px'))
                    arr[i][j] = 0;
                }
                if(arr[i][j] == 7 && p2 == true) {
                    char2MapPos = {y:i,x:j, name:'mspacman', moveCT:0, score:0};
                    char2DispPos = {y:(i * 32),x:(j * 32 )};
                    $("#mspacman").css('top', (char2DispPos.y + 'px'))
                    $("#mspacman").css('left', (char2DispPos.x + 'px'))
                    arr[i][j] = 0;
                }
            }
        }
    }
    
    function drawGhosts(arr) {
        names = ['clyde', 'inky', 'pinky', 'red'];
        for(i = 0; i < arr.length; i++) {
            for(j = 0; j < arr[i].length; j++) {
                if(arr[i][j] == 8) {
                    var id = "#" + names[ghostsInPlay];
                    ghostsMapPos.push({y:i, x:j, moveCT:4, name:names[ghostsInPlay], direction:0});
                    ghostsDispPos.push({y:(i * 32),x:(j * 32 )});
                    $(id).css('top', (ghostsDispPos[ghostsInPlay].y + 'px'))
                    $(id).css('left', (ghostsDispPos[ghostsInPlay].x + 'px'))
                    arr[i][j] = 0;
                    ghostsInPlay++;
                }
            }
        }
    }
    
    function move(mapPos, dispPos, direction, map) {
        var id = "#" + mapPos.name;
        if(map[mapPos.y - 1][mapPos.x] != 1 && direction == 'up') {
            mapPos.moveCT++;
            dispPos.y -= 8;
            $(id).css('top', (dispPos.y + 'px'))
            if(mapPos.moveCT == 4) {
                mapPos.y--;
                mapPos.moveCT = 0;
            }
        } else if(map[mapPos.y + 1][mapPos.x] != 1 && direction == 'down') {
            mapPos.moveCT++;
            dispPos.y += 8;
            $(id).css('top', (dispPos.y + 'px'))
            if(mapPos.moveCT == 4) {
                mapPos.y++;
                mapPos.moveCT = 0;
            }
        } else if(map[mapPos.y][mapPos.x - 1] != 1 && direction == 'left') {
            mapPos.moveCT++;
            dispPos.x -= 8;
            $(id).css('left', (dispPos.x + 'px'))
            if(mapPos.moveCT == 4) {
                mapPos.x--;
                mapPos.moveCT = 0;
            }
        } else if(map[mapPos.y][mapPos.x + 1] != 1 && direction == 'right') {
            mapPos.moveCT++;
            dispPos.x += 8;
            $(id).css('left', (dispPos.x + 'px'))
            if(mapPos.moveCT == 4) {
                mapPos.x++;
                mapPos.moveCT = 0;
            }
        }
    }
    
    function directGhosts() {
        for(i = 0; i < ghostsDispPos.length; i++) {
            var ghostDir = Math.floor(Math.random() * 4)
            if(ghostDir == 0 && ghostsMapPos[i].moveCT > 3) {
                ghostsMapPos[i].direction = 'up'
            } else if(ghostDir == '1' && ghostsMapPos[i].moveCT > 3) {
                ghostsMapPos[i].direction = 'down'
            } else if(ghostDir == '2' && ghostsMapPos[i].moveCT > 3) {
                ghostsMapPos[i].direction = 'left'
            } else if(ghostDir == '3' && ghostsMapPos[i].moveCT > 3) {
                ghostsMapPos[i].direction = 'right'
            }
        }
        ghostsMoves = 0;
    }

    function moveGhosts() {
        for(i = 0; i < ghostsDispPos.length; i++) {
            move(ghostsMapPos[i], ghostsDispPos[i], ghostsMapPos[i].direction, map);
            console.log(ghostsMapPos[i], ghostsDispPos[i], ghostsMapPos[i].direction, map);
        }
        ghostsMoves++
    }
    
    function locCheck(mapPos, p2 = false) {
        if(!p2) {
            if(map[mapPos.y][mapPos.x] == 2){
                mapPos.score += 10;
                map[mapPos.y][mapPos.x] = 0;
            } else if(map[mapPos.y][mapPos.x] == 3){
                mapPos.score += 50;
                map[mapPos.y][mapPos.x] = 0;
            } else if(mapPos.x > map[0].length){
                charMapPos.x = 0;
                charDispPos.x = 0;
            } else if(mapPos.x < 0){
                charMapPos.x = map[0].length;
                charDispPos.x = (map[0].length * 32);
            }
        } else if (p2) {
            if(map[mapPos.y][mapPos.x] == 2){
                mapPos.score += 10;
                map[mapPos.y][mapPos.x] = 0;
            } else if(map[mapPos.y][mapPos.x] == 3){
                mapPos.score += 50;
                map[mapPos.y][mapPos.x] = 0;
            } else if(mapPos.x > map[0].length){
                char2MapPos.x = 0;
                char2DispPos.x = 0;
            } else if(mapPos.x < 0){
                char2MapPos.x = map[0].length;
                char2DispPos.x = (map[0].length * 32);
            }
        }
    }

    function updateScore() {
        $("#charScore").text(charMapPos.score)
        $("#char2Score").text(char2MapPos.score)
    }

    function gameLoop(){
        move(charMapPos, charDispPos, charDirection, map);
        locCheck(charMapPos);
        if(ghostsDispPos.length > 0) {
            if(ghostsMoves > 3) {
                directGhosts()
            }
            moveGhosts();
        }
        drawMap(map);
        updateScore();
    }
    
    function startGame(map) {
        drawMap(map);
        drawPacman(map);
        setTimeout(function() {
            drawGhosts(map);
        }, 5000);
        setInterval(function() {
            gameLoop();
        }, 100);
    }
    
    function start2PGame(map) {
        drawMap(map);
        drawPacman(map, true);
        setTimeout(function() {
            drawGhosts(map);
        }, 5000);
        setInterval(function() {
            move(char2MapPos, char2DispPos, char2Direction, map);
            locCheck(char2MapPos, true)
            gameLoop();
        }, 100);
    }

    document.onkeydown = function(key) {
        if(key.keyCode == 87 && charDispPos.y % 32 == 0  && charDispPos.x % 32 == 0) {         //***'W' -up-***//
            charDirection = 'up';
            $("#pacman").css('transform', 'rotate(270deg)')
        } else if(key.keyCode == 65 && charDispPos.y % 32 == 0  && charDispPos.x % 32 == 0) {  //***'A' -left-***//
            charDirection = 'left';
            $("#pacman").css('transform', 'rotate(180deg)')
        } else if(key.keyCode == 83 && charDispPos.y % 32 == 0  && charDispPos.x % 32 == 0) {  //***'S' -down-***//
            charDirection = 'down';
            $("#pacman").css('transform', 'rotate(90deg)')
        } else if(key.keyCode == 68 && charDispPos.y % 32 == 0  && charDispPos.x % 32 == 0) {  //***'D' -right-***//
            charDirection = 'right';
            $("#pacman").css('transform', 'rotate(0deg)')
        } else if(key.keyCode == 38 && char2DispPos.y % 32 == 0  && char2DispPos.x % 32 == 0) { //**MISS pacman moves** up
            char2Direction = 'up';
            $("#mspacman").css('transform', 'rotate(90deg)')
        } else if(key.keyCode == 37 && char2DispPos.y % 32 == 0  && char2DispPos.x % 32 == 0) { //left
            char2Direction = 'left';
            $("#mspacman").css('transform', 'rotate(0deg)')
        } else if(key.keyCode == 40 && char2DispPos.y % 32 == 0  && char2DispPos.x % 32 == 0) { //down
            char2Direction = 'down';
            $("#mspacman").css('transform', 'rotate(270deg)')
        } else if(key.keyCode == 39 && char2DispPos.y % 32 == 0  && char2DispPos.x % 32 == 0) { //right
            char2Direction = 'right';
            $("#mspacman").css('transform', 'scaleX(-1)')
        }
    };

    $("#p1game").on('click', function() {
        $("#frame").after('<img id="pacman" src="pacman.gif"></img>')
        $("#frame").after('<img id="inky" src="ghostinky.gif" class="ghost"></img>')
        $("#frame").after('<img id="pinky" src="ghostpinky.gif" class="ghost"></img>')
        $("#frame").after('<img id="clyde" src="ghostclyde.gif" class="ghost"></img>')
        $("#frame").after('<img id="red" src="ghostred.gif" class="ghost"></img>')
        startGame(map1);
        // nomSong.play();
    })
    $("#p2game").on('click', function() {
        $("#frame").after('<img id="pacman" src="pacman.gif"></img>')
        $("#frame").after('<img id="mspacman" src="mspacman.gif"></img>')
        $("#frame").after('<img id="inky" src="ghostinky.gif" class="ghost"></img>')
        $("#frame").after('<img id="pinky" src="ghostpinky.gif" class="ghost"></img>')
        $("#frame").after('<img id="clyde" src="ghostclyde.gif" class="ghost"></img>')
        $("#frame").after('<img id="red" src="ghostred.gif" class="ghost"></img>')
        start2PGame(map1);
        // nomSong.play();
    })
})