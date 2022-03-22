

console.log(isMakeTriangle(6,7,11));
console.log(isMakeTriangle(6,7,14));


function isMakeTriangle(a,b,c){
    let max = a;

    if(max < b){
        max = b;
    }

    if(max < c){
        max = c;
    }

    if(a+b+c > 2*max){
        return true;
    }else{
        return false;
    }
}