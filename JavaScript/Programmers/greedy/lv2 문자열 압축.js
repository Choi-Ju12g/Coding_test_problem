function solution(s) {
    let answer = s.length;
  
    for (let unit = 1; unit <= parseInt(s.length / 2); unit++) {
      let answerStr = "";
      let cnt = 1;
      let targetStr = s.substr(0, unit);
      let idx = 0;
  
      for (idx = unit; idx <= s.length; idx += unit) {
        let nextStr = s.substr(idx, unit);
  
        if (targetStr === nextStr) {
          cnt += 1;
        } else {
          if (cnt === 1) answerStr = answerStr + targetStr;
          else answerStr = answerStr + cnt + targetStr;
  
          cnt = 1;
          targetStr = nextStr;
        }
      }
      if (cnt === 1) answerStr = answerStr + targetStr;
      else answerStr = answerStr + cnt + targetStr;
      answer = Math.min(answer, answerStr.length);
    }
  
    return answer;
  }


list =["aabbaccc",
"ababcdcdababcdcd",
"abcabcdede",
"abcabcabcabcdededededede",
"xababcdcdababcdcd"]
answer = [7,9,8,14,17]
