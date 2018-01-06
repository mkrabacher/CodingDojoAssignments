var HOUR = 12,
    MINUTE = 00,
    PERIOD = "AM",
    TOD = "";

if (PERIOD == "AM") {
    TOD = ' in the morning'
} else if (PERIOD == "PM" && HOUR < 5) {
    TOD = ' in the afternoon'
} else if (PERIOD == "PM" && HOUR > 5) {
    TOD = ' at night'
}

if (HOUR == 12 && MINUTE == 00) {
    if (PERIOD == 'AM') {
        console.log("Dude! are you drunk?! it's midnight go to bed!")
    } else if (PERIOD == 'PM') {
        console.log("Lunchtime! FUCK YES! best part of the day.")
    }
} else if (MINUTE == 15) {
    console.log("it's quarter after *err0r*INSERT HOUR HERE*err0r*" + TOD + ".")
} else if (MINUTE == 30) {
    console.log("it's half past " + HOUR + TOD + ".")
} else if (MINUTE == 45) {
    console.log("it's quarter till " + (HOUR + 1) + TOD + ".")
} else if (MINUTE > 30) {
    console.log("It's " + (60 - MINUTE) + " till " + (HOUR + 1) + TOD + ".")
} else if (MINUTE < 30) {
    console.log("It's " + MINUTE + " past " + HOUR + TOD + ".")
}