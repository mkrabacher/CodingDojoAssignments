var monies = 0.01,
    days = 0;

for(i = 0; days < 1030; i++) {
    monies = monies * 2;
    days++;
}

//Takes 20 days to get to 10,485.76. Takes 37 days to get to 1,374,389,534.72. This is not the answer I expected, it takes 1031 days to get to infinite money(Infinity). Huh.

console.log(days);
console.log(monies);