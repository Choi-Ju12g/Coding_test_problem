function solution(n, lost, reserve) {
    for(let i = 0 ; i< reserve.length;i++){
        let haslost = lost.some((el)=> el == reserve[i])
        if (haslost){
            lost = lost.filter((el)=> el !== reserve[i])
            reserve[i] = 0;
        }
    }
    reserve = reserve.filter(v=>v)

    for(let i = 0 ; i< reserve.length;i++){
        for(let j = 0 ; j< lost.length;j++){
            if (Math.abs(reserve[i]-lost[j])<=1){
                reserve[i] = 0
                lost[j] = 0
                break;
            }
        }

    }
    return n - lost.filter(v=>v).length
}