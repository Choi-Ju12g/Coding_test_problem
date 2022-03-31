function solution(new_id) {
    let answer = new_id;
    
    // 1단계
    answer = answer.toLowerCase();
    console.log(answer);
    // 2단계
    answer = answer.replace(/[^\w-.]/g, '');
    console.log(answer);
    // 3단계
    answer = answer.replace(/[\.]{2,}/g,'.');
    //answer = answer.replace(/\.+/g, '.') // 3
    console.log(answer);
    // // 4단계
    answer = answer.replace(/^\.|\.$/g, '');
    console.log(answer);
    // 5단계
    if(!answer.length){
        answer = 'a';
    }
    console.log(answer);
    // // 6단계
    if(answer.length > 15){
        answer = answer.slice(0,15).replace(/\.$/,'');
    }
    console.log(answer);
    // // 7단계
    if(answer.length < 3){
        answer += answer.charAt(answer.length -1).repeat(3- answer.length);
    }
    console.log(answer);
    return answer;
}


// padEnd 풀이
const solution = (new_id) => {
    const id = new_id
        .toLowerCase()
        .replace(/[^\w\d-_.]/g, '')
        .replace(/\.{2,}/g, '.')
        .replace(/^\.|\.$/g, '')
        .padEnd(1, 'a')
        .slice(0, 15)
        .replace(/^\.|\.$/g, '')        
    return id.padEnd(3, id[id.length-1])
}

solution("...!@BaT#*..y.abcdefghijklm.");