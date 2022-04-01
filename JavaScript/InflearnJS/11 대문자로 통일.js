// toLowerCase, toUpperCase
function solution(s){
    let ans = "";
    for (let string of s){
        if(string === string.toLowerCase()) ans += string.toUpperCase();
        else ans += string;
    }
    return ans;
}

function sol(s){
    return s.split('').map(e => {return e.toUpperCase()}).join("");
}

console.log(solution("ItisTimeToStudy"));
console.log(sol("ItisTimeToStudy"));