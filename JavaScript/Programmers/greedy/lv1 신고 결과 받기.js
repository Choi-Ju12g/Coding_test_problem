const list = ["muzi", "frodo", "apeach", "neo"];
const report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","muzi frodo"];

function sol(report){
    let reports = [...new Set(report)].map(a=> {return a.split(' ')});
    return reports 
}

function solution(id_list, report, k) {
    let answer = Array.from({length: id_list.length}, (i) => 0);
    const reportObject = {};
    
    id_list.map((user) => {
        reportObject[user] = [];
    });
    
    report.map((user) => {
        const [report, reported] = user.split(' ');
        if(!reportObject[reported].includes(report)){
            reportObject[reported].push(report);
        }
    })
    
    for(let i = 0; i<id_list.length; i++){
        if(reportObject[id_list[i]].length >= k){
            reportObject[id_list[i]].map((user) => {
                answer[id_list.indexOf(user)] += 1;
            })
        }
    }
    
    return answer;
}

console.log(sol(report));
//console.log(solution(list));

let a = 1
console.log(a+=1);