/* 
 * `codeOwnersMap`과 `directory`를 입력받아
 * `directory`의 코드 주인 목록을 반환하는 함수를 작성하세요.
 */
function solution(codeOwnersMap, directory) {
    const dir = directory.split('/');
    const len = dir.length;
    let dataMap = {...codeOwnersMap};
    
    let answer = []

    for(let i =0; i< len; i++){
        answer = dataMap[dir[i]];
        dataMap = {...dataMap[dir[i]]}
    }
    
    return answer
}

const codeOwnersMap = 
{
    scripts: [ '배수진' ],
    services: {
      'business-ledger': [ '고찬균', '배수진' ],
      'toss-card': [ '채주민', '유재섭' ],
      subsidy: [ '허주엽' ],
      payments: [ '유재섭' ],
      other: { test: [Array] }
    },
    libraries: {
      'yarn-workspaces-plugin-since': [ '유재섭', '배수진' ],
      tds: [ '유병솔', '강두한' ]
    }
  }

  const directory = ['scripts', 'services/subsidy','services/other/test']