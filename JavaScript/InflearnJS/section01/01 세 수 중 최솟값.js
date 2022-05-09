
console.log(minNumber(1,2,3));
console.log(minNumber(1,3,2));
console.log(minNumber(2,1,3));
console.log(minNumber(2,3,1));
console.log(minNumber(3,2,1));
console.log(minNumber(3,1,2));


function minNumber(a,b,c){
    let answer = a;
    
    if(answer > b){
        answer = b;
    }
    
    if(answer > c){
        answer = c;
    }
    return answer;
}

console.log(maxNumber(1,2,3));
console.log(maxNumber(1,3,2));
console.log(maxNumber(2,1,3));
console.log(maxNumber(2,3,1));
console.log(maxNumber(3,2,1));
console.log(maxNumber(3,1,2));


function maxNumber(a,b,c){
    let answer = a;

    if(answer < b){
        answer = b;
    }

    if(answer < c){
        answer = c;
    }
    return answer;
}