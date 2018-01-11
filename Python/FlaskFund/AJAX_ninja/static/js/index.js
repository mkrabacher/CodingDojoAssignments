$(document).ready(function() {
    $("#image").append('<img id=ninja src="127.0.0.1:5000/ninja/red>')

    function getNinja(color) {
        $.get('http://localhost:5000/ninja/' + color, function(res) {
            $("#image").html('<img id="ninja" src="' + res.ninja + '">')
            console.log(res.quote)
            $("#caption").text(res.quote)
        }, 'json')
    }

    $('#red').on('click',function() {
        getNinja('red')
    });
    
    $('#blue').on('click',function() {
        getNinja('blue')
    });
    
    $('#orange').on('click',function() {
        getNinja('orange')
    });
    
    $('#purple').on('click',function() {
        getNinja('purple')
    });
    
    $('#submit').on('click',function() {
        getNinja('april')
    });
    
});