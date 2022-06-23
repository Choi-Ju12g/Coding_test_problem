function solution(s){  
    let answer="";

    for(let i=0; i<s.length; i++){
        //console.log(s[i], i, s.indexOf(s[i]));
        if(s.indexOf(s[i])===i) answer+=s[i];
    }
    return answer;
}

function solution2(s){
    let answer = new Set(s);

    return [...answer].join('');
}
console.log(solution2("ksekkset"));
console.log(solution2('apple'));