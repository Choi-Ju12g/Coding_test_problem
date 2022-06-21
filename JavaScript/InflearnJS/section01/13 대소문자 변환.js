let str = "StuDY";

function solution(str){
    let answer = '';

    for(char of str){
        if(char !== char.toUpperCase()) {
            answer += char.toUpperCase();
        }
        else answer += char.toLowerCase();
    }
    
    return answer;
}

console.log(solution(str));