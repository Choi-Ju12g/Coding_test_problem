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

function solution(n, lost, reserve) {

    // 체육복을 잃어버렸으면서 여벌이 없는 경우
    const realLost = lost.filter((element) => !reserve.includes(element));

    // 여벌이 있으면서 체육복을 잃어버리지 않은 경우
    let realReserve = reserve.filter((element) => !lost.includes(element));

    // 학생 수(n) - 잃어버린 학생이 여벌을 못받은 경우(realLost.filter)
    return (
        // realLost.filter((lost) : 잃어버린 사람 중 여벌을 받을 수 없는 학생을 배열로 반환
        n -
        realLost.filter((lost) => {
            // lend : 체육복을 빌려줄 수 있는 경우 중 첫 번째 요소
            const lend = realReserve.find(
                // 잃어버린 사람의 1칸 주위에 빌릴 사람이 있는 경우
                (reverse) => Math.abs(reverse - lost) == 1,
            );

            // 빌려줄 수 있는 사람이 없으면 진짜 잃어버린 걸로 간주하고 lost를 return
            if (!lend) return lost;
            // 빌려 줬으면 reserve 배열에서 빌려준 사람 제외
            realReserve = realReserve.filter((reverse) => reverse !== lend);
        }).length
    );
}