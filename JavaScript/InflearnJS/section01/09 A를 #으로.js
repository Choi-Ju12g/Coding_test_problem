console.log(solution("BANANA"));
 
// 1. split() + map()
function solution(s){
    s = s.split("").map((item) => item === "A" ? "#" : item)
    return s.join("");
}
 
// 2. for - of
function solution2(s){
    let answer = "";
    for (let i of s){
        if (i === "A") answer += "#"
        else answer += i
    }
 
    return answer;
}
 
// 3. replace + reg
function solution3(s){
    let answer = s;
    answer = answer.replace(/A/g, "#");
 
    return answer;
}