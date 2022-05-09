
function solution(arr){
    let answer = arr;
    let sum = answer.reduce((a,b) => a+b,0);
    const target = sum - 100;
    console.log(target, typeof(target));
    for(let i = 0; i<8; i++){
        for(let j = i+1 ; j<9; j++){
            console.log(answer[i],typeof(answer[i]));
            if(answer[i]+answer[j] == target){
                answer.splice(j,1);
                answer.splice(i,1);
            }
        }
    }
    return answer;
}

let arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(arr));

