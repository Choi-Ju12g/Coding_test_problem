//const lodash = require('lodash');


const arr = Array.from({length: 10}, (v,i) => i+1);
console.log(arr);
function solution(arr){
    let oddArr = arr.filter((e) =>  e %2 !== 0);
    console.log(oddArr);
    let sum = oddArr.reduce((acc,cur) => {return acc + cur}, 0);

    return sum;
}

//console.info(lodash.sum(arr));

console.log(solution(arr));