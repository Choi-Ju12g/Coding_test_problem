function solution(board, moves) {
    let answer = 0;
    let result = [];
    
    // 모든 움직임 검색하기.
    for(let i=0; i<moves.length; i++){
        let col = moves[i]-1;   
       
        for(let j=0; j<board.length; j++){            
            // 인형을 발견하면 집는다.
            if(board[j][col] !== 0){
                if(result[(result.length)-1] === board[j][col]){
                    result.pop();
                    answer += 2;
                }
                else{
                    result.push(board[j][col]);
                }
                
                board[j][col] = 0;                
                break;
            }
        }
    }
    
    return answer;
}