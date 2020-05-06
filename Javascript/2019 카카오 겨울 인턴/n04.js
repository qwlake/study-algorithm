function solution(k, room_number) {
    let answer = [];
    let link = new Map();
    let tmp;
    let tmp_list;
    room_number.forEach(e => {
        if (!link.has(e)) {
            link.set(e, e+1);
            answer.push(e);
        } else {
            tmp = e;
            tmp_list = [];
            while (link.has(tmp)) {
                tmp_list.push(tmp);
                tmp = link.get(tmp);
            }
            link.set(tmp, tmp + 1);
            tmp_list.forEach(t => {
                link.set(t, tmp + 1);
            });
            answer.push(tmp);
        }
        console.log(link);
    });
    return answer;
}

// console.log(solution( // result [1,3,4,2,5,6]
//     10, 
//     [1,3,4,1,3,1]
// ));
console.log(solution( // result [1,2,3,4,5,6,7,8,9]
    100, 
    [1,1,1,1,5,5,5,5,3]
));