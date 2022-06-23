

function solution(str){
    let answer;
    let mid = Math.floor(str.length/2);

    if(str.length % 2 === 0){
        answer = str.substring(mid-1,mid+1);
    }else{
        answer = str.substring(mid, mid+1);
    }

    return answer;
}

console.log(solution("study"));
console.log(solution('good'));

// substr 과 substring 차이 substr(시작인덱스 , 개수)  substring(시작인덱스, 최종인덱스)-> 당연히 포함 미포함