const lottos = [44, 1, 0, 0, 31, 25];
const win_nums = [31, 10, 45, 1, 6, 19];

function solution(lottos, win_nums) {
    let answer = [];
    let lotto = [...new Set(lottos)]
    const zeroCount = lottos.filter(i => i === 0).length;
    let correctCount = 0;
    
    for(const num of win_nums){
        if(lotto.includes(num)){
            correctCount += 1;
        }
    }
    
    answer = [7-correctCount-zeroCount, 7-correctCount].map(i => {
        if(i === 7){
            return 6;
        }else{
            return i;
        }
    });
    
    return answer;
}