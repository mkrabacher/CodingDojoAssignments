var nuts = 4;

function numbersOnly(arr) {
    var newArr = [],
        len =  arr.length;

    for(i = 0; i < len; i++) {
        console.log(len);
        if(typeof arr[i] === "number") {
            newArr.push(arr[i]);
            arr.splice(i, 1);
            i -= 1;
        }
    }
    return newArr;
}

console.log(numbersOnly([1, "asdf", true, nuts, 55, 33]));