function printRange(start, end = start, skip = 1) {
    if(start == end) {
        start = 0;
    }
    for(i = start; i < end; i += skip) {
        console.log(i)
    }
}

console.log('-----------------------')
printRange(2, 10, 2)
console.log('-----------------------')
printRange(-2, 10, 2)
console.log('-----------------------')
printRange(2, 10)
console.log('-----------------------')
printRange(2)
console.log('-----------------------')