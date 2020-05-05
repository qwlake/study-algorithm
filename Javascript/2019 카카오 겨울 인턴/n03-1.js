function loop(bans, idx, filterd) {
    let ret = new Set();
    if (filterd.length === bans.length) {
        let tmp = filterd.slice();
        tmp = tmp.sort().join('');
        ret.add(tmp);
    } else {
        let res;
        for (let i = 0; i < bans[idx].length; i++) {
            if (!filterd.includes(bans[idx][i])) {
                filterd.push(bans[idx][i]);
                res = loop(bans, idx+1, filterd);
                res.forEach(function(e) {
                    ret.add(e);
                });
                filterd.pop();
            }
        }
    }
    return ret;
}
function solution(user_id, banned_id) {
    let answer = 0;
    const re = (a, b) =>
        new RegExp(`^${b}$`).test(a);
    for (let i = 0; i < banned_id.length; i++) {
        banned_id[i] = banned_id[i].replace(/\*/g, '.');
    }
    let bans_list = [];
    banned_id.forEach(b => {
        bans_list.push(user_id.filter(u => re(u, b)));
    });
    answer = loop(bans_list, 0, []);
    return answer.size;
}

console.log(solution( // result 2
    ["frodo", "fradi", "crodo", "abc123", "frodoc"], 
    ["fr*d*", "abc1**"]
));
console.log(solution( // result 2
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["*rodo", "*rodo", "******"]
));
console.log(solution( // result 3
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"]
));