
const arr = [5,3,7,11,4,16,72,18];

//console.log(findMinValue(arr));


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

function solution4(arr){
    arr.sort((a,b) => a-b);
    return arr[0]
}

console.log(solution4(arr));