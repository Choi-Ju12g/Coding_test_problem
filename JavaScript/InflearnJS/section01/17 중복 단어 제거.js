let str=["good", "time", "good", "time", "student"];


function solution(str){
    let answer = new Set(str);

    let sol1 = [...answer];
    let sol2 = Array.from(answer);
    let sol3 = [];
    answer.forEach((v) => sol3.push(v));
    return sol1, sol2, sol3;
}

function solution2(s){  
    let answer;
    console.log(s.indexOf("time"));
    answer=s.filter((v, i)=>{
        console.log(s.indexOf(v), i);
        if(s.indexOf(v)===i) return v;
    });
 
    return answer;
}

// indexOf 는 처음 만나는 인덱스를 반환하기 때문에 가능한 방식
console.log(solution(str));
