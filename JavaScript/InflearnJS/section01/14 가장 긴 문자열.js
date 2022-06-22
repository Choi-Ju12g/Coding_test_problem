let str=["teacher", "time", "student", "beautiful", "good"];
            
function solution(str){
    let answer = '';

    for(string of str){
        if(string.length > answer.length) answer = string;
    }
    return answer
}

console.log(solution(str));