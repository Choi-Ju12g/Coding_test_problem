console.log(solution("COMPUTERPROGRAMMING", "G"));
 
// for - of
function solution(s, target){
    let cnt = 0;
    for (let i of s){
        if (i === target) cnt += 1
    }
    return cnt;
}
 
// split
function solution(s, target){
    let answer = s.split(target);
    return answer.length - 1 ;
}