function solution(s) {
    let answer = new Set();
    s = s.slice(1, s.length-1);
    let arr = [];
    let tmpArr = [];
    let tmp;
    let intSt;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '{') {
            intSt = i+1;
        } else if ((s[i] === ',' || s[i] === '}') && intSt !== -1) {
            tmp = parseInt(s.slice(intSt, i));
            tmpArr.push(tmp);
            intSt = i+1;
        }
        if (s[i] === '}') {
            arr.push(tmpArr);
            tmpArr = [];
            intSt = -1;
        }
    }

    arr.sort(function(a, b) {
        return a.length - b.length;
    });

    arr.forEach(e => {
        tmp = e.filter(x => !answer.has(x));
        answer.add(tmp[0]);
    });
    
    return Array.from(answer);
}

console.log(solution(
    "{{2},{2,1},{2,1,3},{2,1,3,4}}", 
));

console.log(solution(
    "{{20,111},{111}}",
));