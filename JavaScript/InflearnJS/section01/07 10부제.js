let day = 3;
let cars = [12, 20, 54, 33, 87, 91, 30];
 
console.log(solution(day, cars));
 
function solution(day, cars){
    return cars.filter((car) => car % 10 === day).length;
};


function solution2(day, cars){
    return cars.filter((e) => e % 10 === day).length;
}