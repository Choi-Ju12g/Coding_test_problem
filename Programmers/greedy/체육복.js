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

unction solution(n, lost, reserve) {

    // reserve의 얇은 복사본
    // slice()를 쓰면 reserve가 변할 때 tmp가 변하지 않지만
    // splice()를 쓰면 reserver가 변할 때 tmp가 변한다.
    let tmp = reserve.slice();

    for (let i in tmp) {
        // 잃어 버린 학생이 여분이 있는 학생인지 확인
        let key = lost.indexOf(tmp[i]);

        // 여분이 없으면 여분이 있는 학생이 잃어버린 학생에게 빌려준다
        if (key != -1) {
            lost.splice(key, 1);
            reserve.splice(reserve.indexOf(tmp[i]), 1);
        }
    }

    for (let i of reserve) {
        // 잃어버린 사람 한 칸 주위에 여분이 있는 사람이 있는지
        let key = lost.includes(i - 1)
            ? lost.indexOf(i - 1)
            : lost.indexOf(i + 1);

        // 있으면 잃어버린 사람 배열에서 삭제
        if (key != -1) {
            lost.splice(key, 1);
        }
    }

    return n - lost.length;
}
