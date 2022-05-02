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

function solution(new_id) {
    var answer = '';
    
    // 1단계
    new_id = new_id.toLowerCase();
    // 2단계
    for(let i=0; i<new_id.length; i++){
        if( 'a'<= new_id[i] && new_id[i] <='z'){
            answer += new_id[i];
        }
        else if( '0' <= new_id[i] && new_id[i] <= '9'){
            answer += new_id[i];
        }            
        else if(new_id[i] === '-' || new_id[i] === '_' || new_id[i] === '.'){
            answer += new_id[i];
        }        
    }    
    // 3단계
    answer = answer.replace(/\.{2,}/g, '.');        
    // 4단계
    if(answer[0] === '.')
        answer = answer.slice(1,answer.length)
    if(answer[answer.length-1] === '.')
        answer = answer.slice(0,answer.length-1);    
    // 5단계
    if(answer === '')
        answer += 'a';    
    // 6단계
    if(answer.length >= 16){
        answer = answer.slice(0,15);
        if(answer[answer.length-1] === '.')
            answer = answer.slice(0, answer.length-1);
    }
    console.log(answer);
    // 7단계
    if(answer.length <= 2){
        while(1){
            answer += answer[answer.length-1]
            if(answer.length >= 3)
                break;
        }
    }
    console.log(answer)
    
    return answer;
}