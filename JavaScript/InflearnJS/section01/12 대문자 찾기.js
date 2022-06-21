const str = "KoreaTimeGood";

function solution(str){
    let answer = 0;

    for(char of str){
        //let num=x.charCodeAt();
        //if(num>=65 && num<=90) answer++;
        if(char===char.toUpperCase()) answer++; 
    }

    return answer;
}

console.log(solution(str));