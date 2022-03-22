
const arr = [1,2,3,4,5,6,7,8];

console.log(findMinValue(arr));


function findMinValue(arr){
    const a = Math.min(...arr);
    return a;
}

function solution2(...arr){
    let min = Number.MAX_SAFE_INTEGER;

    arr.forEach((e) => {
        if(e < min){
            min = e;
        }
    })
    
    return min;
}

function solution3(...arr){
    return Math.min.apply(null, arr);
}