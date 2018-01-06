
$(document).ready(function() {
    function display_data(data) {
        console.dir(data)
        var volNum = 1,
        html = '';
        for(i = 0; i < data.length; i += 50) {
            if(data[i + 50]) {
                html += '<h3>Vol ' + volNum + ': ' + data[i].date.substring(0,10) + ' to ' + data[i + 49].date.substring(0, 10) + '</h3><div id="' + volNum + '" class="vol">';
                for(j = i; j < i + 50; j++) {
                    html += ('<h3>' + data[j].date.substring(0,10) + ', ' + data[j].country + '</h3><div><p>Country: ' + data[j].country + ', ' + data[j].location + '</p><p>Lat:' + data[j].lat + ', Lon:' + data[j].lon + '</p><p>Total killed: ' + data[j].deaths + '</p><p>Summary: ' + data[j].bij_summary_short + '</p><p>Bureau of Investigative Journalism: <a href="' + data[j].bij_link + '">' + data[j].bij_link + '</a></p></div>')
                }
            } else {
                html += ('<h3>Vol ' + volNum + ': ' + data[i].date.substring(0,10) + ' to ' + data[data.length -1].date.substring(0, 10) + '</h3><div id="' + volNum + '" class="vol">')
                for(j = i; j < data.length -1; j++) {
                    html += ('<h3>' + data[j].date.substring(0,10) + ', ' + data[j].country + '</h3><div><p>Country: ' + data[j].country + ', ' + data[j].location + '</p><p>Lat:' + data[j].lat + ', Lon:' + data[j].lon + '</p><p>Total killed: ' + data[j].deaths + '</p><p>Summary: ' + data[j].bij_summary_short + '</p><p>Bureau of Investigative Journalism: <a href="' + data[j].bij_link + '">' + data[j].bij_link + '</a></p></div>')
                }
            }
            html += '</div>';
            volNum++
        }
        return html;
    }

    var urlstring = 'http://api.dronestre.am/data';
    function get(bool) {
        $.get(urlstring, function(res) {
            var data = res.strike;
            $("#drone-table").html(display_data(data));

            if(bool) {
                if($("#country").val() != 'all'){
                    console.log(data[0]['country'])
                    data = data.filter(entry => entry['country'] == $("#country").val())
                }
            }
            
            $(function() {
                $(".vol").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                });
                $("#drone-table").accordion({
                    collapsible: true,
                    heightStyle: 'content'
                });
            });
        }, 'json')
    }

    get(false)

    //slider function and controls
    $(function() {
        function date_maker(num) {
            var years = 0,
                months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                month = 0;
                num += 11;
            while(num > 0) {
                if(num > 12) {
                    years += 1;
                    num -= 12
                } else {
                    month += 1
                    num -= 1
                }
            }
            return `${years + 2002} - ${months[month - 1]}`
        }

        $("#slider-range").slider({
        range: true,
        min: 0,
        max: 171,
        values: [0, 161],
        slide: function(event, ui) {
            $("#dates").val(date_maker(ui.values[0]) + " to " + date_maker(ui.values[1]));
        }
        });
        $("#dates").val("2002 - Nov to 2017 - Mar");
    });
    


    $("#search-btn").click(function(){
        $("#drone-table").html("<h3>loading...</h3>");
        get(false)
    })
});